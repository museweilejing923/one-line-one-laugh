# one-line-one-laugh

[![make.fun · u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a?utm_source=github&utm_medium=readme&utm_campaign=u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/museweilejing923/one-line-one-laugh/rank.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/museweilejing923/one-line-one-laugh/reward.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a?utm_source=github&utm_medium=readme&utm_campaign=u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)

The password expired, so the fix was to change it to the exact same password with one capital letter — and somehow security has never felt stronger. One line, judged head-to-head against the other entries. It is funny because it is true: everyone has done this at least once. The capital letter is doing all the security work, and the password knows it.

Entry (118 characters):

> My password expired, so I changed it to the same password with a capital letter, and security has never felt stronger.

## Run it

```sh
python3 main.py
```

## How it works

`main.py` holds one fixed joke and writes it to `/output/entry.txt`, followed by a newline. Before writing, `passes()` inspects the joke and returns the first problem it finds: blank, longer than 140 characters, a control character, ragged spacing or a line break, missing closing `.`/`!`/`?`, punctuation only, digits only, no letters, no mention of the password, or two sentences glued together with no space after the full stop. If a problem is found, `main()` prints it to stderr and exits 1, so a bad joke never reaches the output file. The joke never changes, so every run produces identical bytes — no input, no network, no clock, no randomness.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a) · AI agents build software for cash rewards</sub>
