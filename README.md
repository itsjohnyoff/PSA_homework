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

## Problem 3: Labouchere Roulette System
One of the most popular casino games is roulette. Many people like roulette because it is easy to learn and play. Because the game is simple, many betting systems have been proposed to "guarantee" profit. One of them is the **Labouchere system**.

### Problem Statement
Start with the list:

- `1, 2, 3, 4`

At each step:

1. Bet the sum of the first and last entries (for example, `1 + 4 = 5`) on red.
2. If you win, delete the first and last numbers from the list.
3. If you lose, append the amount you just bet to the end of the list.
4. If the list has one number left, bet that number.
5. Continue until the list is empty.

You are asked to show that if the list becomes empty, your net gain is the sum of the original list:

- `1 + 2 + 3 + 4 = 10`

Then simulate the system and investigate whether it always stops (and therefore always wins). If not, explain why this is not a foolproof gambling strategy.

### Simulation Assumptions (Problem 3)
- Initial list: `[1, 2, 3, 4]`
- Target profit: `$10`
- Bankroll: `$1000`
- Table limit: `$500`
- European roulette wheel (`18/37` chance to win a red bet)

### How to Run (Problem 3)
Use Python 3:

```bash
python Problem_3.py
```

Then choose:
- `1` to watch one full game step by step.
- `2` to run many games and estimate win rate and net profit.
- `q` to quit.

### Why It Is Not Foolproof
Even if the system wins small amounts frequently, losing streaks can make the required next bet grow quickly. In real casinos, bankroll limits and table limits can stop the sequence before recovery, leading to rare but very large losses.
