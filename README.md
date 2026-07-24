# Can't Stop

A clone of the classic push-your-luck dice game **Can't Stop**, written in
[Hollywood](https://www.hollywood-mal.com/) (the Amiga multimedia language).

## Features

- 1–4 players, hotseat **plus computer opponents (AI)**
- German 🇩🇪 and English 🇬🇧 (switchable in the start menu)
- Start menu with rules screen
- **Classic board:** columns 2–12 use the original track lengths
  (2→3, 3→5, 4→7, 5→9, 6→11, 7→13, 8→11, 9→9, 10→7, 11→5, 12→3)
- **Bust-risk indicator:** shows the exact probability that your next roll
  busts, colour-coded (green / orange / magenta) and aware of how many
  runners you still have free
- Runners are white-circle **sprites** (flicker-free movement over a static
  board) with a highlight frame on your active columns; captured columns take
  the owner's colour
- Animated dice roll and runner moves, with sound effects
  (roll / bust / place / win) — native 8SVX audio on Amiga
- Winner's columns blink on victory
- Mouse-driven UI (buttons for rolling, placing, ending a turn)
- **Fullscreen toggle (Amiga only):** a *Fullscreen / Window* button — in the
  start menu and in-game (bottom-left) — switches the Amiga version between
  windowed and scaled fullscreen via `ChangeDisplayMode`; the Windows build is
  unaffected

## Downloads

Ready-to-run binaries are attached to each
[release](https://github.com/phipslk/cantstop/releases/latest):

| Asset | Platform |
|-------|----------|
| `cantstop.exe` | Windows (embedded die icon) |
| `cantstop68k` | Amiga 68k (68020+, AmigaOS 3.x, needs RTG) |
| `cantstop68k.info` | Amiga Workbench program icon + `NOLEGACYAUDIO` tooltype |
| `cantstop.hws` | Hollywood source |

## Repository contents

The repository holds the source and its build assets — the compiled binaries
live only on the releases page, not in the repo:

| File | Description |
|------|-------------|
| `cantstop.hws` | Hollywood source code |
| `runner.png`, `title.png` | Runner sprite + title screen (embedded in the binaries) |
| `icon_color.png`, `icon_color_sel.png` | Source images for the Amiga colour icon |
| `cantstop68k.info` | Amiga Workbench program icon (colour die) + `NOLEGACYAUDIO` tooltype |
| `CantStop.info` | Amiga Workbench drawer icon |
| `dice.wav`, `bust.wav`, `win.wav`, `place.wav` | Sound effects (Windows/desktop build) |
| `dice.8svx`, `bust.8svx`, `win.8svx`, `place.8svx` | Sound effects (Amiga 8SVX build) |

## Running

- **Windows:** download `cantstop.exe` from the
  [releases page](https://github.com/phipslk/cantstop/releases/latest) and run it
- **Amiga (68k):** download `cantstop68k` (keep `cantstop68k.info` next to it so
  Workbench shows the die icon). Sound uses AHI; the icon's `NOLEGACYAUDIO`
  tooltype selects Hollywood's new AHI driver, which is required for
  AHI-over-emulation setups (e.g. AmiKit / WinUAE). From a Shell, launch with
  `-nolegacyaudio` instead. Use the *Fullscreen / Window* button (start menu
  or bottom-left in-game) to switch to a scaled fullscreen display and back —
  it needs an RTG screen, which the game already requires.
- **From source:** open `cantstop.hws` with Hollywood. Keep `runner.png`,
  `title.png` and the sound files next to the script — the `.wav` files for a
  Windows/desktop
  build, the `.8svx` files for an Amiga build (the script picks the right set
  per target via `@IF #HW_AMIGA`).

## How to play (short)

Reach the top of **3 columns** (numbered 2–12) before your opponents.
Each turn you roll 4 dice, split them into two pairs, and advance up to
**3 runners**. After each roll you may keep going (risking a *bust* that
loses this turn's progress) or bank your progress and end your turn. The
bust-risk tile helps you decide when to stop. A column you reach the top of
and bank becomes yours — and closed for everyone.

The in-game **Rules** screen explains everything in your selected language.
