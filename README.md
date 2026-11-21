# DR Disso Vision Guard

**Author: DR Disso** | **Status: research prototype / demonstration**

Authorized CCTV camera health and integrity monitoring.

## Capabilities

- Explainable rules-based risk assessment using authorized, locally supplied JSON data.
- Browser-based interface (`web/index.html`) with JavaScript evaluation; no network requests.
- Python 3.9+ analysis CLI, JSON reporting and automated unit tests.
- Editable policy rules in `rules.json` and sample synthetic data.
- GitHub Actions tests on push and pull requests.
- MIT license, security policy and documented limitations.

## Quick start

```powershell
python engine.py data/sample.json
python -m unittest discover -s tests -v
```

Open `web/index.html` locally for the browser interface. The browser demo has built-in example rules; update `web/app.js` when you change `rules.json`.

## Scope and safety

This prototype does **not** contain production AI models, sensor integrations, real-time collection, antivirus removal, financial decision automation, satellite connectivity, camera control, or agency-specific integrations. No connection to NASA, FBI, White House, police or any government agency is claimed. Real integrations require approved hardware, documented APIs, consent, audit logging and independent security validation. All input must be lawfully obtained.

## Roadmap

1. Authenticated, consent-based sensor connectors and data validation.
2. Time-series baselines and evaluated, explainable machine-learning models.
3. Encrypted fleet reporting with role-based access and audit logs.
4. Signed release artifacts, supply-chain scanning and integration tests.
5. Threat modeling, performance benchmarking and independent security review.

## Languages

Python 3 for the analyzer; JavaScript, HTML and CSS for the local browser interface; YAML for CI.

## License

MIT © 2026 DR Disso.
