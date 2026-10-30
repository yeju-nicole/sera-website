# SERA website

Live site: https://yeju-nicole.github.io/sera-website/

A single-file, bilingual (한국어 / English) site for SERA, built from the SERA Charter (v1.0 draft) and the SERA Principles (v1.1, 2026-10-09).

## Files

- `index.html`: the whole site. Upload it anywhere that serves static files (it needs no server code). Fonts load from Google Fonts.
- `source/`: the content and build script. Text lives in `content.py` as (Korean, English) pairs; run `python3 source/build.py <out_dir>` to regenerate `index.html` (copy the result over the old one).

## Pages and links

The site is one page with three views, chosen by the link's `#` part:

| Link | Shows |
| --- | --- |
| `index.html` | Home: about, the four principles, the cycle, SERAship, records, declaration, glossary |
| `index.html#charter` | Full SERA Charter |
| `index.html#principles` | Full SERA Principles |
| `index.html#c-4`, `#p-21` | A single article (c = Charter, p = Principles) |

Language: Korean by default. Add `?lang=en` to open in English (e.g. `index.html?lang=en#charter`). A visitor's choice is remembered in their browser.

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

- The English text is a translation for reference; the page says the Korean original is authoritative.
- Footer contact (address, sdx@sdxfoundation.org) was taken from sdxfoundation.org on 2026-10-30.
