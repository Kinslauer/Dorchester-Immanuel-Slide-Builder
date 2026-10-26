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

## How it's built

- `src/template.html`: the page (HTML, CSS and script).
- `src/songs.json`: the starting song list, pulled from the Sunday decks in the "Song Backup" Drive folder (January 2025 to October 2026). Each entry is `{t: title, k: "song" | "hymn", s: [slide text], u: times used, d: last used}`.
- `src/assets/`: the Welcome slide pictures from those decks.
- `vendor/pptxgen.bundle.js`: [PptxGenJS](https://github.com/gitbrent/PptxGenJS) 3.12.0 (MIT), which writes the .pptx file in the browser.
- `build.py`: inlines all of the above into `index.html`, so the page is one self-contained file.

After changing anything in `src/`, run `python3 build.py` and commit the new `index.html`.

## Hosting

GitHub Pages serves `index.html` from the `main` branch: **Settings → Pages → Deploy from a branch → `main` / `(root)`**.
The page then lives at `https://kinslauer.github.io/Dorchester-Immanuel-Slide-Builder/`.
`index.html` also works offline: download it and double-click it.
