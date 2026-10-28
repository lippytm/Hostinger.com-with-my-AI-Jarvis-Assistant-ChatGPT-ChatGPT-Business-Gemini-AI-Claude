# Recover existing Jarvis connections without reinstalling

Owner: the existing VPS/runtime operator. Risk: high for deployment or credentials.

The previous installer cloned
`lippytm/aievolutionaryevolutions.com-Hermes-Fabric-MemPalace-` and ran npm and a
root-level `server.js`. That repository's inspected default branch has neither
`package.json` nor `server.js`. It is not a deployable Node application.
Rerunning that installer cannot restore an existing connection.

The retained `scripts/jarvis-master-install.sh` now performs source preflight only.
It does not install packages, create users, change firewalls, run unreviewed remote
scripts, print credentials, replace proxies, or restart existing workers.
Calling it without a checkout path fails explicitly before any machine changes.

## Reuse the actual existing runtime

The established implementation is in
`lippytm/AI-Jarvis-Assistant-ChatGPT-Gemini-AI-GitHub-Claude-and-all-of-my-Repositories-DOG-Dog-dog-`.
Keep a complete checkout: `runtime/` depends on `config/prompt-11-profile.json`.

```bash
bash scripts/jarvis-master-install.sh /absolute/path/to/full-jarvis-checkout
```

In that checkout, follow `runtime/README.md`. Run `npm run check` and `npm test`
from `runtime/`. Start the existing service only after checking whether another
instance already owns its port. Its documented default is loopback port 8787,
not the old installer's assumed root-level app on port 3001.
Keep `JARVIS_DRY_RUN=true` and `JARVIS_ALLOW_EXTERNAL=false` initially.
The runtime is an advisory pilot, not a remote execution worker or public service.

Use the existing `src/jarvis/hostinger.py` and
`docs/HERMES_MEMPALACE_HOSTINGER.md` for owner-approved read-only Hostinger
inventory. It requires `HOSTINGER_API_TOKEN` and explicit external opt-in.
Inventory does not verify VPS health, site ownership, DNS, or publishing rights.

## Verification before claiming recovery

- [ ] Record the authoritative deployment repository/revision and owner privately.
- [ ] Preserve the current service, proxy, DNS, private environment, and data.
- [ ] Check the actual service's documented health and authenticated dry-run route.
- [ ] Validate each provider separately using an approved non-sensitive task.
- [ ] Verify a bundle with the existing Jarvis bundle verifier before handoff.
- [ ] Check the actual domain DNS/TLS separately; do not overwrite records blindly.

Past connections can exist even when this repository has no active deployment
workflow. Source-only checks and a green audit do not prove current live access.
Never commit tokens, private keys, account inventories, or provider responses.

Rollback: stop only a newly started pilot, restore the previous reviewed source
revision if needed, and retain prior service/data. Do not rerun the retired
installer for rollback. Support: use the owning runtime's redacted error/status
and Hostinger support for account, DNS, or VPS access problems.
