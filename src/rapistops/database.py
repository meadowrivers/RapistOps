"""Database connection management.

Connection parameters are read from the environment so that credentials are
never committed to the repository. Either set ``DATABASE_URL`` to a full
libpq/psycopg connection string, or set the individual ``PG*`` variables
documented in ``.env.example``.

Two access patterns are provided:

* :func:`transaction` — the preferred path for application code. It borrows a
  connection from a shared pool, yields a cursor, commits on success, rolls
  back on error, and always returns the connection to the pool.
* :func:`get_connection` — a standalone (non-pooled) connection for callers
  that need to manage their own lifecycle (e.g. test fixtures).
"""

from __future__ import annotations

import os
from collections.abc import Iterator
from contextlib import contextmanager

import psycopg
from psycopg import Connection, Cursor
from psycopg.conninfo import make_conninfo
from psycopg_pool import ConnectionPool

_pool: ConnectionPool | None = None


def _conninfo() -> str:
    """Build a libpq connection string from the environment."""
    url = os.environ.get("DATABASE_URL")
    if url:
        return url

    params: dict[str, str] = {
        "host": os.environ.get("PGHOST", "localhost"),
        "port": os.environ.get("PGPORT", "5432"),
        "dbname": os.environ.get("PGDATABASE", "rapistops"),
        "user": os.environ.get("PGUSER", "meadow"),
    }

    password = os.environ.get("PGPASSWORD")
    if password:
        params["password"] = password

    # Default to requiring TLS unless explicitly overridden.
    params["sslmode"] = os.environ.get("PGSSLMODE", "prefer")

    return make_conninfo(**params)


def get_pool() -> ConnectionPool:
    """Return the process-wide connection pool, creating it on first use."""
    global _pool
    if _pool is None:
        _pool = ConnectionPool(
            conninfo=_conninfo(),
            min_size=int(os.environ.get("RAPISTOPS_DB_POOL_MIN", "1")),
            max_size=int(os.environ.get("RAPISTOPS_DB_POOL_MAX", "10")),
            open=True,
        )
    return _pool


def close_pool() -> None:
    """Close the shared pool. Intended for shutdown and test teardown."""
    global _pool
    if _pool is not None:
        _pool.close()
        _pool = None


@contextmanager
def transaction() -> Iterator[Cursor]:
    """Yield a cursor inside a pooled transaction.

    The transaction is committed if the block exits normally and rolled back
    if it raises. The connection is always returned to the pool.
    """
    with get_pool().connection() as connection, connection.cursor() as cursor:
        yield cursor


def get_connection() -> Connection:
    """Open a new standalone connection using the configured parameters.

    Callers are responsible for committing/closing. Prefer :func:`transaction`
    for application code.
    """
    return psycopg.connect(_conninfo())
