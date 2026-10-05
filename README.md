# Houston's First Brand

The public source of truth for **Houston's First Baptist Church** brand standards: identity, colors, typography, voice, and writing style. It's built so people *and* AI tools can produce consistent, on-brand work.

> **Status:** v1.1.0. Content authority: Houston's First **Communications Team**. Maintained by the Development Team.

## For AI agents

1. Use **[`brand-tokens.json`](brand-tokens.json)** for any color, font, or type value. Never guess a hex code. Use the `semantic.*` tokens for UI.
2. Read **[`voice-and-tone.md`](voice-and-tone.md)** before writing copy, and run its review checklist before returning.
3. Check every name, date, time, and capitalization against **[`writing-style-guide.md`](writing-style-guide.md)**.
4. For visual decisions (logo, color, type, accessibility, imagery), follow **[`brand-guide.md`](brand-guide.md)**.
5. Every link and CTA points to **HoustonsFirst.org**. Never write "HFBC" in public copy.
6. If a rule isn't covered, say so. Don't invent one.

## Key files

| File | What it is |
|---|---|
| [`brand-guide.md`](brand-guide.md) | Mission, vision, strategy, traits, audiences, logo, color, typography, **digital accessibility**, digital destination, AI imagery |
| [`brand-tokens.json`](brand-tokens.json) | Colors, fonts, and type roles as W3C design tokens (print and digital pairings) |
| [`voice-and-tone.md`](voice-and-tone.md) | How we sound: traits as voice, tone by audience, moment, and channel; approved messaging; review checklist |
| [`writing-style-guide.md`](writing-style-guide.md) | Church, campus, ministry, and event names; dates; times; divine terms; dashes; addresses |
| [`assets/`](assets/README.md) | Logo exports and font guidance (licensed fonts are not included) |

Coming: `spanish-brand-guidelines.md` (Houston's First Spanish Brand Guidelines).

## Quick reference

| | |
|---|---|
| Church name | Houston's First Baptist Church · Houston's First |
| Website | HoustonsFirst.org |
| Mission | The Great Commission (Matthew 28:19–20) |
| Vision | relevant biblical community |
| Strategy | Gather, Grow, Give |
| Traits | Generous · Vibrant · Relational · Attentive · Genuine |
| Core colors | Slate `#1A303A` · Navy `#00365B` · Sky `#40A2D8` · Gray `#EDEEEF` |
| Accents | Apricot `#FE7A36` · Kelly `#4CB963` |
| Type | Gibson (primary) · Tisa Pro (subheads) · Futura PT Condensed (compact) |
| Logo | Black or white only |

## Brand site

`index.html` is a one-page brand site (colors, accessibility, type, logo rules, writing quick rules) published with **GitHub Pages**. It reads its colors from an embedded copy of `brand-tokens.json`, so after changing the tokens or `VERSION`, run:

```sh
python3 scripts/embed-tokens.py
```

CI fails if the page is out of date. `.nojekyll` makes Pages serve the raw `.md`/`.json` files too, so agents can fetch e.g. `/brand-tokens.json` directly.

**Turn it on:** Settings → Pages → Deploy from a branch → `main` / `(root)`. Optional custom domain: add a `CNAME` file (e.g., `brand.houstonsfirst.org`), create a DNS CNAME record pointing to `houstonsfirst.github.io`, enable **Enforce HTTPS**, and verify `houstonsfirst.org` in the org's Pages settings.

## Using this repo from other projects

Consume a **tagged release** (e.g., `v1.0.0`), not `main`, so updates are deliberate. Houston's First's internal tooling pins a version and updates it by pull request.

## Versioning

Semantic versioning, recorded in [`VERSION`](VERSION) and [`CHANGELOG.md`](CHANGELOG.md):

- **Major:** a rule changes meaning (e.g., a color or name is replaced)
- **Minor:** new rules or sections (e.g., Spanish Brand Guidelines)
- **Patch:** clarifications, typos, formatting

## Usage rights

© Houston's First Baptist Church. All rights reserved. Shared publicly for reference by staff, volunteers, vendors, and partners producing work *for* Houston's First. See [`LICENSE.md`](LICENSE.md).

**Maintainers:** Nguyen Nguyen, Yesu Chum (Development Team) · **Content authority:** Communications Team
