# SERA website

Live site: https://yeju-nicole.github.io/sera-website/

A single-file, bilingual (한국어 / English) site for SERA, built from the SERA Charter (v1.0 draft), the SERA Principles (v1.1, 2026-10-09), the SDX SERA brochure and SERA 0.0.1 (2026-10-19).

## Files

- `index.html`: the whole site. Upload it anywhere that serves static files (it needs no server code). Fonts load from Google Fonts.
- `source/`: the content and build script. Page copy lives in `sections.py` (concise) and `content.py` (source text) as (Korean, English) pairs; run `python3 source/build.py <out_dir>` to regenerate `index.html` (copy the result over the old one).

## Sections

One page, Korean by default. Section links: `#about`, `#four`, `#way`, `#promises`, `#records`, `#together`, `#salimist`, `#declaration`, `#glossary`. Add `?lang=en` to open in English (e.g. `index.html?lang=en#way`). A visitor's language choice is remembered in their browser.

## What is deliberately not published

This is a public site, so internal material from the source documents is left out:

- Full text of the SERA Charter (v1.0 draft) and SERA Principles (v1.1): drafts with internal governance (amendment and board procedures, operating regulations, certification committee and record-hashing details, duties for unreleased SERA Agent / My SERA Agent products). Their public-facing ideas are summarized instead.
- SERA 0.0.1: research hypotheses and validation plans, pilot design, system architecture (GESIA CCS, Always-On Agent design), AI vendor comparisons and third-party statistics. Only the participant-facing principles (the five promises, what SERA does not treat as a problem, separating who wrote a record) are used.
- The named partner in the SERA Art case is shown as an unnamed example.
- The digital platform roadmap (SERA Profile, Journey, AI Companion, Network) is not described as a product.

## Attaching it to the SDX Foundation site

Option A, link (simplest): host the file at e.g. `sera.sdxfoundation.org` or `sdxfoundation.org/sera/`, then add a "SERA" item to the SDX menu pointing to it. The SERA header already links back to sdxfoundation.org, and the footer links to SDX About, Themes, Sponsor and Contact.

Option B, embed: put it inside an SDX page with an iframe. `?embed=1` hides the SERA top bar and footer so it sits inside the SDX layout. The page reports its height to the parent so the frame can grow to fit:

```html
<iframe id="sera" src="https://YOUR-HOST/sera/index.html?embed=1" style="width:100%;border:0;min-height:900px" title="SERA"></iframe>
<script>
  window.addEventListener("message", function (e) {
    if (e.data && e.data.type === "sera:height") document.getElementById("sera").style.height = e.data.height + "px";
  });
</script>
```

Links back to SDX open in the full window (`target="_top"`), not inside the frame.

## Notes

- The English text is a translation of the Korean source documents.
- Footer contact (address, sdx@sdxfoundation.org) was taken from sdxfoundation.org on 2026-10-30.
