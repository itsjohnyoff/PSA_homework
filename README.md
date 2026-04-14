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
The script in `Problem_1.py` simulates repeated games:
- One game: flip a fair coin until first heads, then compute payout `2^j`.
- Many games: run the game repeatedly and compute the average payout.
- Sweep mode: test multiple sample sizes (`10` to `1,000,000`) to observe how the average changes.

## How to Run
Use Python 3:

```bash
python Problem_1.py
```

Then choose:
- `1` to run the sweep of predefined game counts.
- `2` to run a custom number of games.
- `q` to quit.

## Notes
The expected value of the game is theoretically unbounded, but simulations over finite samples usually produce moderate averages most of the time, with rare very large payouts. This is why practical willingness to pay per game can depend strongly on the number of plays and risk tolerance.

## Problem 2: I bet my life on this one
Russian roulette setup:
- Revolver with 6 slots and 2 bullets.
- First trigger pull is a click (you survived).
- You must choose the second pull strategy:
	1. Spin the barrel, then pull.
	2. Do not spin, just pull the next chamber.

The assignment requires probabilities for both strategies in multiple configurations:
- 6 slots, bullets adjacent.
- 6 slots, bullets not adjacent.
- 5 slots, bullets adjacent.
- 5 slots, bullets not adjacent.

For each configuration, there are two outcomes to compute (spin vs no spin), for a total of 8 reported probabilities.

### Simulation Approach (Problem 2)
The script in `Problem_2.py` simulates conditional probability after surviving the first trigger:
- Randomly choose the first chamber position.
- Discard timelines where the first shot would have killed you.
- On surviving timelines, simulate the second shot for:
	- no spin (next chamber), and
	- spin (random chamber).
- Estimate death probability as:
	- deaths on second shot / valid surviving timelines.

### How to Run (Problem 2)
Use Python 3:

```bash
python Problem_2.py
```

Then choose:
- `1` to run all scenarios and print the 8 probabilities.
- `q` to quit.
