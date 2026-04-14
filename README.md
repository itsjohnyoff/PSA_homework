# PSA Homework

## Problem 1: How much should I bet?
A fair coin is flipped until it lands on heads for the first time.
If heads appears on the `j`-th toss, the payout is:

- $2^j$ dollars

You are guaranteed to win at least $2, but the practical question is:

- How much is it reasonable to pay per game?
- Does this amount depend on how many games you can play?

This is the classic **St. Petersburg paradox**, explored here by simulation.

## Simulation Approach
The script in `1.py` simulates repeated games:
- One game: flip a fair coin until first heads, then compute payout `2^j`.
- Many games: run the game repeatedly and compute the average payout.
- Sweep mode: test multiple sample sizes (`10` to `1,000,000`) to observe how the average changes.

## How to Run
Use Python 3:

```bash
python 1.py
```

Then choose:
- `1` to run the sweep of predefined game counts.
- `2` to run a custom number of games.
- `q` to quit.

## Notes
The expected value of the game is theoretically unbounded, but simulations over finite samples usually produce moderate averages most of the time, with rare very large payouts. This is why practical willingness to pay per game can depend strongly on the number of plays and risk tolerance.
