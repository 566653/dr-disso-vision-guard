# Operations and security

This release is an offline rules-based prototype, not a production-grade autonomous security product.

## Data handling
Use synthetic or explicitly authorized input. Do not commit sensitive records. The Python CLI does not transmit data. Browser interface processes pasted JSON locally.

## Deployment
Run the unit tests before deploying. Review `rules.json` for false positives and missed threats. Only trusted maintainers should merge changes to the main branch.

## Updating
GitHub Actions tests run on each push and pull request. Dependabot checks GitHub Actions dependencies weekly and proposes reviewable pull requests; updates are **not** installed silently.

## Collaboration
External contributors should fork, branch and open pull requests. Maintainers review code and security impact before merge. Enable GitHub branch protection and security advisories in repository settings where available.

## Planned
Authenticated connectors, real-time collection, secure audit logs, encryption and independently evaluated ML models. None are claimed as deployed.
