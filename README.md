# Dorchester Immanuel Slide Builder

A web page that builds the Sunday PowerPoint for Dorchester Immanuel Church of the Nazarene.
There is nothing to install: open the page, pick the songs, and press **Make my PowerPoint**.

## Using it

1. **Pick this Sunday's songs.** Search the song list by name or by words in the lyrics, then tap a song to add it.
   *Type in a new song* adds a song that isn't in the list (a blank line starts a new slide).
   *Hymn from the book* adds a single title slide, such as "Amazing Grace #92 (Hymn)".
   *Change words* edits a song, and the change is kept for later weeks.
2. **Choose how the words look.** Pick the background (black and white taking turns is the default), the size of the words, the letters, and bold. The preview shows each slide as it will look.
3. **Welcome and announcements.** The Welcome slide goes at the start and end (black with logo, or the church photo). Each announcement becomes its own slide after the Welcome slide.

**Make my PowerPoint** downloads one 4:3 deck named like `Sunday 11-1-2026.pptx`. The words shrink automatically so every slide fits.

Changes and new songs are saved in the browser that made them. **Save a backup of my songs** downloads a file that **Restore from a backup** can load on another computer or browser.

## Sunday Live (running the service)

`live.html` replaces MediaShout and BibleShow on Sunday morning: one page that shows songs, hymn title cards, scripture, announcements and welcome slides on the projector.

1. **Build the service order** on the left. Add songs from the song list, scripture from the Bible tab, your own slides, a welcome slide or a countdown to the start of service. Drag items or use the arrows to reorder them. **Bring in this week's songs from Sunday Slides** copies what was picked in the builder.
2. **Open projector screen** opens a second window. Drag it onto the projector and double-click it to fill the screen. In Chrome or Edge, if the computer allows it, the window opens on the projector by itself. **Stage view** opens a window for the musicians or the pastor. It shows the words on screen now, the next slide, and a clock.
3. **Run it.** Click any slide to show it, or use the keys: <kbd>→</kbd>/<kbd>Space</kbd>/<kbd>Page Down</kbd> for next, <kbd>←</kbd>/<kbd>Page Up</kbd> for back (so a presentation clicker works), <kbd>B</kbd> for a black screen, <kbd>L</kbd> for the logo, and <kbd>C</kbd> to hide the words but keep the background.

**Bible:** type a reference such as `jn 3:16`, `Ps 23`, `1 cor 13:4-7` or `Rom 8:38-9:2`, then press <kbd>Enter</kbd> to show it or <kbd>Shift</kbd>+<kbd>Enter</kbd> to add it to the service. You can also type a few words to find a verse. While scripture is on screen, <kbd>↑</kbd>/<kbd>↓</kbd> move one verse back or forward through the Bible. The translation can be switched while a verse is showing. The page includes the **KJV** and the **Berean Standard Bible**. Both are public domain. The NKJV, NIV and ESV are copyrighted and can't be included.

**Look:** songs, scripture and other slides each have their own background (colors, gradients, the church pictures, or your own picture), word color, letters, size, shadow and alignment. Changes show on the projector right away. The screen shape can be 4:3 or 16:9.

**Save service** downloads the service order (with its look and pictures) as a file. Open that file on the church computer with **Open service**. Song changes are shared with the Sunday Slides builder when both pages are opened in the same browser.

## How it's built

- `src/template.html`: the page (HTML, CSS and script).
- `src/songs.json`: the starting song list, pulled from the Sunday decks in the "Song Backup" Drive folder (January 2025 to October 2026). Each entry is `{t: title, k: "song" | "hymn", s: [slide text], u: times used, d: last used}`.
- `src/assets/`: the Welcome slide pictures from those decks.
- `vendor/pptxgen.bundle.js`: [PptxGenJS](https://github.com/gitbrent/PptxGenJS) 3.12.0 (MIT), which writes the .pptx file in the browser.
- `src/live.html`: the Sunday Live page.
- `src/bible/*.json.gz`: the KJV and Berean Standard Bible text (public domain, from [scrollmapper/bible_databases](https://github.com/scrollmapper/bible_databases)). It was made by `tools/make_bibles.py`.
- `build.py`: inlines all of the above into `index.html` and `live.html`, so each page is one self-contained file.

After changing anything in `src/`, run `python3 build.py` and commit the new `index.html` and `live.html`.

## Hosting

GitHub Pages serves `index.html` from the `main` branch: **Settings → Pages → Deploy from a branch → `main` / `(root)`**.
The page then lives at `https://kinslauer.github.io/Dorchester-Immanuel-Slide-Builder/`.
`index.html` also works offline: download it and double-click it.
