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

4. **Look over every slide.** The whole PowerPoint is shown in order. Tap any slide to give it its own background (a color, a soft gradient, the church pictures, or your own picture), for that slide only or for every slide of the song.

**Most lines on one slide** (in step 2) splits long slides so the words can be bigger.

**Make my PowerPoint** downloads one 4:3 deck named like `Sunday 11-1-2026.pptx`. The words shrink automatically so every slide fits.

**Open a PowerPoint to change it** (in step 1) opens a PowerPoint made with this page, on any computer, so it can be changed and made again. Each PowerPoint carries its plan inside (songs, words, look and own pictures). Older ones are rebuilt from their slides.

Google Slides files work too: in Slides choose **File → Download → Microsoft PowerPoint (.pptx)** and open that. If the words were changed in PowerPoint or Google Slides, the changed words are kept.

### Open from Google Drive (optional, one-time setup)

The **Open from Google Drive** button stays hidden until the page has a Google sign-in key. Google requires these to come from the account that owns the app, so they can't be built in. To set it up (about 10 minutes, free):

1. Go to https://console.cloud.google.com, create a project (for example "Sunday Slides"), and note its **project number** on the dashboard.
2. **APIs & Services → Library**: turn on the **Google Drive API** and the **Google Picker API**.
3. **APIs & Services → OAuth consent screen**: choose *External*, fill in the app name and your email, add the scope `.../auth/drive.file`, then **Publish app** (this scope doesn't need Google's review).
4. **APIs & Services → Credentials → Create credentials → OAuth client ID**: type *Web application*, and under *Authorized JavaScript origins* add `https://kinslauer.github.io`.
5. **Create credentials → API key**, and restrict it to the Google Picker API.
6. Put the three values in `src/template.html` in `const GOOGLE = { clientId: "...", apiKey: "...", appId: "<project number>" }`, run `python3 build.py`, and commit.

The page only asks for access to the files you pick, not your whole Drive.

Changes and new songs are saved in the browser that made them. **Save a backup of my songs** downloads a file that **Restore from a backup** can load on another computer or browser.

## Sunday Live (running the service)

`live.html` replaces MediaShout and BibleShow on Sunday morning: one page that shows songs, hymn title cards, scripture, announcements and welcome slides on the projector.

1. **Build the service order** on the left. Add songs from the song list, scripture from the Bible tab, your own slides, a welcome slide or a countdown to the start of service. Drag items or use the arrows to reorder them. **Bring in this week's songs from Sunday Slides** copies what was picked in the builder.
2. **Open projector screen** opens a second window. Drag it onto the projector and double-click it to fill the screen. In Chrome or Edge, if the computer allows it, the window opens on the projector by itself. **Stage view** opens a window for the musicians or the pastor. It shows the words on screen now, the next slide, and a clock.
3. **Run it.** Click any slide to show it, or use the keys. <kbd>Space</kbd> (or <kbd>Enter</kbd> or <kbd>Page Down</kbd>, so a presentation clicker works) puts the "Up next" slide on the projector. The arrow keys only change what's up next on the operator screen, so you can look ahead or jump to another slide or verse without the room seeing it; press <kbd>Space</kbd> to show it. <kbd>Page Up</kbd> goes back one slide on the projector. <kbd>F2</kbd> sends the projector window to the other monitor and fills it. <kbd>B</kbd> is a black screen, <kbd>L</kbd> the logo, and <kbd>C</kbd> hides the words but keeps the background.

**Bible:** start typing a book and it offers matches as you type (`1 th` → 1 Thessalonians, `thes` → both letters). Press <kbd>Tab</kbd> or <kbd>Enter</kbd> to take one, then pick a chapter and a verse from the buttons that appear. You can also type a whole reference such as `jn 3:16`, `Ps 23`, `1 cor 13:4-7` or `Rom 8:38-9:2`, then press <kbd>Enter</kbd> to show it or <kbd>Shift</kbd>+<kbd>Enter</kbd> to add it to the service. You can also type a few words to find a verse. While scripture is on screen, <kbd>↑</kbd>/<kbd>↓</kbd> move one verse back or forward through the Bible. The translation can be switched while a verse is showing. The page includes the **KJV** and the **Berean Standard Bible**. Both are public domain. The NKJV, NIV and ESV are copyrighted and can't be included.

**Quick find:** <kbd>Ctrl</kbd>+<kbd>K</kbd> finds any song, verse, item in the service or command. <kbd>Enter</kbd> shows it and <kbd>Shift</kbd>+<kbd>Enter</kbd> adds it.

**Loop:** before the service, **Loop** cycles through the announcement and welcome slides every 8 seconds until you press a slide or Next.

**Shorter slides:** in the Look tab, songs and other slides can be limited to 2, 3, 4 or 6 lines, and scripture to about 20, 30 or 45 words. Long verses are split at commas and periods, and <kbd>↓</kbd> walks through the parts.

**Look:** songs, scripture and other slides each have their own background (colors, gradients, the church pictures, or your own picture), word color, letters, size, shadow and alignment. Changes show on the projector right away. The screen shape can be 4:3 or 16:9.

**Menus and toolbar:** like MediaShout, the page has a File / Insert / Live / View / Help menu bar and a toolbar of large icon buttons. It starts in dark mode. **View → Light mode** (or <kbd>Ctrl</kbd>+<kbd>L</kbd>) switches it, and each computer remembers its choice. **Help → Keyboard shortcuts** (or <kbd>?</kbd>) lists the keys.

**Save service** downloads the service order (with its look and pictures) as a file. Open that file on the church computer with **Open service**. Song changes are shared with the Sunday Slides builder when both pages are opened in the same browser.

## Design credits

Both pages borrow ideas from [Magic UI](https://github.com/magicuidesign/magicui) (MIT: dot pattern, border beam, shimmer button, blur fade) and [React Bits](https://github.com/DavidHDev/react-bits) (MIT + Commons Clause: spotlight card, click spark, shiny text). Those libraries are React components. Here the effects are rewritten in a few lines of plain CSS and JavaScript, so the pages stay single files that work offline. In Sunday Live, **View → Turn animations off** stops the moving effects on a slow computer. Both pages also respect the computer's "reduce motion" setting.

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
