# PSA Homework

## Problem 1: How much should I bet?
### Problem Statement
A fair coin is flipped until it lands on heads for the first time. If heads appears on the j-th toss, the payout is $2^j$ dollars.

This is the classic St. Petersburg paradox. The practical questions are:
- How much is it reasonable to pay per game?
- Does this amount depend on how many games you can play?

### Simulation Approach
The script in Problem_1.py simulates repeated games:
- One game: flip a fair coin until first heads, then compute payout `2^j`.
- Many games: run the game repeatedly and compute the average payout.
- Sweep mode: test multiple sample sizes (`10` to `1,000,000`) to observe how the average changes.

### How to Run
Use Python 3:

```bash
python Problem_1.py
```

Then choose:
- `1` to run the sweep of predefined game counts.
- `2` to run a custom number of games.
- `q` to quit.

### Key Takeaway
The expected value of the game is theoretically unbounded, but simulations over finite samples usually produce moderate averages most of the time, with rare very large payouts. This is why practical willingness to pay per game can depend strongly on the number of plays and risk tolerance.

## Problem 2: I bet my life on this one
### Problem Statement
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
The script in Problem_2.py simulates conditional probability after surviving the first trigger:
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

### Key Takeaway
The best decision (spin or no spin) depends on bullet placement and cylinder size. Conditional probability after surviving the first shot changes the risk profile.

## Problem 3: Labouchere Roulette System
### Problem Statement
One of the most popular casino games is roulette. Many people like roulette because it is easy to learn and play. Because the game is simple, many betting systems have been proposed to "guarantee" profit. One of them is the **Labouchere system**.

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

### Simulation Approach
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

### Key Takeaway
Even if the system wins small amounts frequently, losing streaks can make the required next bet grow quickly. In real casinos, bankroll limits and table limits can stop the sequence before recovery, leading to rare but very large losses.

## Problem 4: Oscar's Grind Roulette System
### Problem Statement
Oscar's Grind is another roulette progression strategy. The core idea is to target a small sequence gain (typically +1 unit) by increasing bets only after wins, and keeping the same bet after losses, while trying to recover deficits gradually.

### Simulation Approach
- Session-based simulation over a fixed number of spins.
- Starting bankroll: `$1000`
- Table limit: `$500`
- Win probability per even-money roulette bet (European wheel): `18/37`
- Tracks:
  - final session profit,
  - largest bet reached,
  - worst drawdown,
  - terminal status (`done`, `bankrupt`, or `limit`).

### How to Run (Problem 4)
Use Python 3:

```bash
python Problem_4.py
```

Then choose:
- `1` to watch one 50-spin session step by step.
- `2` to simulate many sessions and print aggregate results.
- `q` to quit.

### Key Takeaway
Oscar's Grind can look stable over short sessions, but exposure still grows during adverse streaks and can be cut off by bankroll or table limits.

## Problem 5: MD5 Birthday Attack Simulation
### Problem Statement
This problem demonstrates the birthday paradox in hash functions by searching for two different inputs that share the same prefix of an MD5 hash.

### Simulation Approach
Find a collision on the first `40` bits of MD5 (equivalent to the first `10` hexadecimal characters) using this method:
- Generate random input strings.
- Compute MD5 digest.
- Keep only the first `10` hex characters.
- Store previously seen prefixes in a dictionary.
- Stop when two different inputs produce the same prefix.

### Output Includes
- elapsed time,
- attempts until collision,
- the two colliding inputs,
- their full MD5 hashes,
- the matching truncated prefix.

### How to Run (Problem 5)
Use Python 3:

```bash
python Problem_5.py
```

Then choose:
- `1` to start the collision search.
- `q` to quit.

### Key Takeaway
Even without breaking full MD5, truncated hashes collide quickly due to the birthday effect, illustrating why short hash prefixes are unsafe for uniqueness.

## Bonus: Map Area Estimator (Monte Carlo)
### Problem Statement
Estimate the area of a red-highlighted region on a map image using random sampling (Monte Carlo darts).

### Simulation Approach
- Load an image file and read pixel colors.
- Throw random sample points uniformly across the image.
- Count a hit when a sampled pixel is red (`r > 100`, `g < 100`, `b < 100`).
- Estimate region ratio as:
  - red_hits / total_samples
- Convert ratio to area using a known total map area (`42.0` square miles in the script).

### Requirements
- Python package: Pillow

Install with:

```bash
pip install pillow
```

### How to Run
Use Python 3:

```bash
python Bonus.py
```

Then provide:
- image filename (for example, `map.png`)
- number of random samples (darts)

The script includes basic safety caps:
- minimum samples reset to `100000` if invalid or non-positive
- maximum samples capped at `5000000`

### Output Includes
- number of red hits
- estimated red percentage
- estimated mined area in square miles

### Key Takeaway
Monte Carlo estimation converges as sample size increases, but results still vary slightly run to run due to randomness.
