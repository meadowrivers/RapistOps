# Security Policy

RapistOps handles exceptionally sensitive information about sexual violence,
survivors, and accused individuals. Security and privacy are treated as part of
the system's core requirements, not as an afterthought. We ask the security
community to engage with us accordingly.

## Supported versions

RapistOps is in early development (pre-1.0). Only the `main` branch receives
security fixes at this stage. There is no production deployment commitment yet;
this policy will tighten as the system matures.

## Reporting a vulnerability

**Please do not open a public GitHub issue for security vulnerabilities, data
exposures, or privacy defects.** Public disclosure of a flaw in a system like
this can directly endanger the people the data describes.

Instead, report privately using one of:

- GitHub's **private vulnerability reporting** for this repository
  (Security tab → "Report a vulnerability"), which is the preferred channel.
- If that is unavailable, contact the maintainer directly through the contact
  listed on the maintainer's GitHub profile.

Please include:

- A description of the issue and its impact.
- Steps to reproduce (proof-of-concept is welcome, but **do not** exfiltrate,
  retain, or publish any real personal data you encounter).
- Any affected endpoints, files, or components.
- Your assessment of severity.

### What to expect

- **Acknowledgement:** we aim to acknowledge a report within a few days.
- **Assessment:** we will confirm the issue, determine severity, and agree on a
  remediation timeline with you.
- **Credit:** we are happy to credit reporters who wish to be named, once a fix
  is available. Coordinated disclosure is expected — please give us a reasonable
  window to remediate before any public write-up.

## Handling of sensitive data during research

Because of the nature of this project, security testing has guardrails:

- **Do not** access, download, retain, or share real personal data about
  identifiable people beyond the minimum needed to demonstrate a flaw.
- **Do not** test against any production or shared data store. Use your own
  local instance with synthetic data.
- **Do not** perform denial-of-service, spam, or load testing against shared
  infrastructure without prior written agreement.
- **Do not** use the system or any discovered flaw to harass, threaten, stalk,
  dox, or re-identify any person. This voids any safe-harbor consideration.
- Report any **accidental** exposure of real personal data immediately and
  delete your copy once the report is acknowledged.

## Safe harbor

If you make a good-faith effort to follow this policy — report privately, avoid
privacy violations and data destruction, and avoid harm to the people the data
describes — we will treat your research as authorized, will not pursue or support
legal action against you for it, and will work with you on remediation. This
safe harbor does not extend to accessing third-party systems, harming
individuals, or retaining/publishing personal data.

## Scope

In scope:

- Source code in this repository.
- The data schema and storage layer.
- CI/CD configuration and dependency supply chain.

Out of scope (report to the relevant provider, not here):

- Third-party services, source websites, or public-records systems that
  RapistOps may collect from.
- Social-engineering of maintainers or contributors.

## Related documents

See [`docs/threat_model.md`](docs/threat_model.md) for the system threat model,
including the domain-specific threats that make this project different from a
typical application and the controls planned to mitigate them.
