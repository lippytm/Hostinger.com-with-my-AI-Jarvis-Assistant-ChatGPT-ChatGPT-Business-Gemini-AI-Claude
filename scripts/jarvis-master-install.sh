#!/usr/bin/env bash
set -euo pipefail

# Retained filename for old bookmarks; installation is no longer automatic.
if [ "$#" -ne 1 ]; then
  printf '%s\n' \
    'The legacy automatic installer is retired: its target repository has no Node application.' \
    'No packages, firewall rules, services, DNS, credentials, or data were changed.' \
    'Usage: bash scripts/jarvis-master-install.sh /absolute/path/to/full-jarvis-checkout' \
    'Use the existing main Jarvis project, including runtime/ and config/.' >&2
  exit 2
fi

checkout=$1
case "$checkout" in
  /*) ;;
  *) printf '%s\n' 'A complete absolute checkout path is required.' >&2; exit 2 ;;
esac
for file in runtime/package.json runtime/src/server.mjs config/prompt-11-profile.json; do
  if [ ! -f "$checkout/$file" ]; then
    printf 'Missing required Jarvis source file: %s\n' "$file" >&2
    printf '%s\n' 'No installation attempted. See docs/EXISTING_CONNECTION_RECOVERY.md.' >&2
    exit 1
  fi
done
if ! command -v node >/dev/null 2>&1; then
  printf '%s\n' 'Node.js 22 or newer is required; install a supported LTS release separately.' >&2
  exit 1
fi
node -e 'if (Number(process.versions.node.split(".")[0]) < 22) process.exit(1)' || {
  printf '%s\n' 'Node.js 22 or newer is required.' >&2
  exit 1
}
node --check "$checkout/runtime/src/server.mjs"
printf '%s\n' \
  'Source preflight passed. No service was installed, restarted, or contacted.' \
  'Follow runtime/README.md in that checkout; start with loopback-only dry-run.' \
  'Run its existing tests before any separately approved deployment.' \
  'This check does not verify tokens, providers, Hostinger, DNS, or account health.'
