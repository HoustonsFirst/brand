# AGENTS.md

Instructions for AI agents working **in** this repository.

## This repo is PUBLIC

Everything here is visible to anyone. Before adding or changing anything, make sure it contains **no**:

- member or staff personal data, or staff email addresses (the generic `Firstname.Lastname@HoustonsFirst.org` format example is fine)
- internal links (Rock admin, Rock Requests, JotForm, SharePoint) or internal tools
- details about church systems or security (Rock plugins, servers, audits)
- internal policies or processes (promotion tiers in detail, AI policy text, glossary of internal terms)

Those belong in the private `houstonsfirst/playbook` repository.

## Ownership

- **Content authority:** Communications Team. They decide what the standards say. Agents may fix formatting, links, and typos; substantive changes must be proposed and confirmed by Communications.
- **Maintainers:** Nguyen Nguyen (`@nguyenernguyener`), Yesu Chum (`@YesuCS`).

## Rules

1. Keep the provenance labels in `voice-and-tone.md` (🟢 Official / 🔵 House guidance / 🟡 Proposed). New agent-written guidance is 🟡.
2. Flag contradictions with a ⚠️ note; don't resolve them silently.
3. Every doc keeps its header table (Source(s) · Content authority · Maintainers · Last reviewed) and its "For AI agents" blockquote.
4. Links stay **inside this repo** or point to public HoustonsFirst.org pages.
5. Never commit licensed font files.
6. Use the `houstonsfirst` prefix for asset file names (e.g., `houstonsfirst-primary-black.svg`).

## Brand site (`index.html`)

- Colors, tints, seasons, and contrast ratios come from the **embedded tokens**. Never hardcode a new color in the page. Edit `brand-tokens.json`, then run `python3 scripts/embed-tokens.py`.
- The page's prose (traits, logo rules, writing quick rules) summarizes the Markdown guides. When those rules change, update the matching section of `index.html` in the same PR.
- The page itself follows §5 Digital accessibility: no white text on Sky; buttons are Navy with white or Sky with Slate.

## Releasing a change

1. Edit, bump **Last reviewed** in changed docs.
2. Bump [`VERSION`](VERSION) (semver, see README) and add a `CHANGELOG.md` entry naming who at Communications confirmed it.
3. After merge, tag `vX.Y.Z`. Downstream repos update their pinned version by pull request.
