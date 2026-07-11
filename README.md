# Can't Stop

A clone of the classic push-your-luck dice game **Can't Stop**, written in
[Hollywood](https://www.hollywood-mal.com/) (the Amiga multimedia language).

## Features

- 1–4 players, hotseat **plus computer opponents (AI)**
- German 🇩🇪 and English 🇬🇧 (switchable in the start menu)
- Start menu with rules screen
- Animated dice roll with sound effects (roll / bust / win)
- Mouse-driven UI (buttons for rolling, placing, ending a turn)

## Files

| File | Description |
|------|-------------|
| `cantstop.hws` | Hollywood source code |
| `cantstop.exe` | Windows binary |
| `cantstop68k.exe` | Amiga (68k) binary |
| `dice.wav`, `bust.wav`, `win.wav` | Sound effects |

## Running

- **Windows:** run `cantstop.exe`
- **Amiga (68k):** run `cantstop68k.exe`
- **From source:** open `cantstop.hws` with Hollywood. The three `.wav`
  files must sit next to the script.

## How to play (short)

Reach the top of **3 columns** (numbered 2–12) before your opponents.
Each turn you roll 4 dice, split them into two pairs, and advance up to
**3 runners**. After each roll you may keep going (risking a *bust* that
loses this turn's progress) or bank your progress and end your turn. A
column you reach the top of and bank becomes yours — and closed for everyone.

The in-game **Rules** screen explains everything in your selected language.
