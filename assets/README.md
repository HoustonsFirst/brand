# Brand Assets

Web-ready exports only. Master design files (`.ai`, `.psd`, `.indd`) stay with the Creative Team. This repo is for SVG and PNG files that people and agents can use directly.

## Logos

Naming: `houstonsfirst[-{campus}]-{lockup}-{variant}.{ext}`. Lockup is `primary` (horizontal), `stacked` (vertical), or `mark`. Variant is `black` for light backgrounds or `white` for dark backgrounds. Campuses share the campuswide mark, so campus folders have no `mark` files.

```
logos/
├── campuswide/
│   ├── houstonsfirst-primary-black.svg     houstonsfirst-primary-white.svg
│   ├── houstonsfirst-stacked-black.svg     houstonsfirst-stacked-white.svg
│   ├── houstonsfirst-mark-black.svg        houstonsfirst-mark-white.svg
│   └── png/                                ← same names, plus @2x
├── loop-campus/
│   ├── houstonsfirst-loop-primary-black.svg    houstonsfirst-loop-primary-white.svg
│   ├── houstonsfirst-loop-stacked-black.svg    houstonsfirst-loop-stacked-white.svg
│   └── png/
├── cypress-campus/                         ← houstonsfirst-cypress-…
├── downtown-campus/                        ← houstonsfirst-downtown-…
└── sienna-campus/                          ← houstonsfirst-sienna-…
```

| Status | File set | Notes |
|---|---|---|
| ☑ | Campuswide: primary, stacked, mark × black/white | |
| ☑ | The Loop Campus: primary, stacked × black/white | |
| ☑ | Cypress Campus: primary, stacked × black/white | |
| ☑ | Downtown Campus: primary, stacked × black/white | |
| ☑ | Sienna Campus: primary, stacked × black/white | |
| n/a | Houston's First en Español | A ministry of The Loop Campus, not a campus, so no campus logo. Add a ministry mark here only if one exists |

### Which file to use

- **Web:** SVG. Each file has `role="img"` and a `<title>`, so it has an accessible name when inlined. Still give `<img>` tags an `alt`.
- **Microsoft Office, email, video:** PNG from `png/`. Transparent background. `@1x` is 150px tall for primary lockups and 300px tall for stacked and mark; `@2x` is double. Scale down only.

### Updating the files

Master files stay with the Creative Team. When they send new SVG exports, rebuild everything here with:

```bash
python3 scripts/build-logos.py path/to/exports
```

The script renames to the convention above, strips editor metadata, sets one fill per file, adds the title, and renders the PNGs. It needs Google Chrome and Pillow (`pip install pillow`).

## Fonts

**Do not commit Gibson, Tisa Pro, or Futura PT files.** They are licensed through Adobe Fonts and can't be redistributed. Load them through the church's Adobe Fonts web project, or use the free alternatives:

| Brand font | Free alternative | Source |
|---|---|---|
| Gibson | Montserrat | [Google Fonts](https://fonts.google.com/specimen/Montserrat) |
| Tisa Pro | Gentium Book Plus | [Google Fonts](https://fonts.google.com/specimen/Gentium+Book+Plus) |
| Futura PT Condensed | Barlow Condensed | [Google Fonts](https://fonts.google.com/specimen/Barlow+Condensed) |

`fonts/` is reserved for open-license (OFL) files only, if offline copies are ever needed.

## Screen and signage specs

From the Promotion Playbook (July 2026). Design screen graphics to be read at a glance.

| Surface | Limit |
|---|---|
| Flatscreens | Max 6 slides in rotation per screen, 8 seconds each |
| Portable LEDs | Max 3 slides in rotation, 8 seconds each |
| Posters | Max 2 per event |

Location matters: place content where its audience already is (for example, Women's events near Preschool check-in).

QR codes and tap tags must resolve to a **HoustonsFirst.org** URL. See [brand guide §7](../brand-guide.md#7-digital-destination).

## Rules (summary)

- Logo is black or white only. Never recolor it.
- Keep clearspace of half the logomark's size on all sides.
- Primary lockup is at least 0.3 in tall; stacked is at least 0.75 in.
- Use the campuswide logo for multi-campus content.

Full rules: [`../brand-guide.md`](../brand-guide.md#4-logo)
