# AI Jarvis Assistant Integration Contract

## Station

- Name: Hostinger
- Owner: Charles Earl Lipshay
- Role: Website assembly, staging, approved deployment, commerce, fulfillment, and public presentation.
- Coordinator: AI Jarvis Assistant
- Canonical control plane: https://github.com/lippytm/AI-Jarvis-Assistant-ChatGPT-Gemini-AI-GitHub-Claude-and-all-of-my-Repositories-DOG-Dog-dog-
- Current connection state: integration draft; authenticated live round trip not yet verified

## Shared work contract

This repository participates in the Unified AI Jarvis Assistant Fabric. Work should enter and leave through versioned handoff packets containing:

- bundle ID, project name and version
- source and destination stations
- requested outcome and changes made
- evidence, tests and unresolved uncertainty
- risks and approval state
- next action and SHA-256 receipt

GitHub is the canonical version and evidence record. Gemini, Claude, ChatGPT and other AI systems contribute through explicit handoffs; repository presence does not imply shared chat memory or live authenticated access.

## Allowed private work

AI stations may research, analyze, draft, test, document, diagnose and propose improvements. Deterministic tests and verified evidence outrank model agreement.

## Owner approval gates

Charles Earl Lipshay must approve merges, deployments, publication, spending, checkout activation, credential access, installations, external messages, deletion, and legal or financial commitments.

## Secrets

Do not commit API keys, passwords, OAuth tokens, customer data or private business records. Credentials belong in an approved secret manager or deployment environment.

## Activation checklist

1. Review and merge the canonical Control Tower foundation.
2. Configure this station with least-privilege credentials outside Git.
3. Run one harmless authenticated round trip.
4. Verify provider identity, bundle ID, timestamp and SHA-256 receipt.
5. Mark the station connected only after the verification passes.

## Read-only connection pilot (September 26, 2026)

The Unified Fabric review branch contains `src/jarvis/hostinger.py`, which calls only Hostinger's documented `GET /api/hosting/v1/websites` endpoint. It requires explicit `allow_external=True` and a `HOSTINGER_API_TOKEN` supplied outside Git. The adapter has no deploy, delete, checkout, or website-edit operation. Its request and simulated response are tested offline; no authenticated account result has been obtained.

On an authorized workstation with a private token, run the read-only inventory and verify the intended account contains `aievolutionaryevolutions.com`. Record a redacted receipt with the request time, endpoint, website identity, and response digest; never record the token or full private account inventory in this public repository. Hostinger AI Website Builder editing remains a separate, unverified integration path.

Canonical implementation and runbook: [Hermes MemPalace Hostinger pilot](https://github.com/lippytm/AI-Jarvis-Assistant-ChatGPT-Gemini-AI-GitHub-Claude-and-all-of-my-Repositories-DOG-Dog-dog-/blob/jarvis/unified-ai-fabric-v0.1/docs/HERMES_MEMPALACE_HOSTINGER.md).
Official API reference: https://docs.hostinger.com/api-reference/overview
