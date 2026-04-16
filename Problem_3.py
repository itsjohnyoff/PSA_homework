import random
import sys

def play_labouchere(verbose=False, bankroll=1000, table_limit=500):
    """Simulates a single full run of the Labouchere system."""
    sequence = [1, 2, 3, 4]
    profit = 0
    spins = 0
    
    while len(sequence) > 0:
        spins += 1
        
        # 1. Determine the bet
        if len(sequence) == 1:
            bet = sequence[0]
        else:
            bet = sequence[0] + sequence[-1]
            
        # 2. Check Reality Limits (Why it's not foolproof)
        if bet > (bankroll + profit):
            if verbose: 
                print(f"  [!] BANKRUPT at spin {spins}. Needed to bet ${bet}, but only had ${bankroll + profit} left.")
            return profit
        
        if bet > table_limit:
            if verbose: 
                print(f"  [!] TABLE LIMIT REACHED at spin {spins}. Needed to bet ${bet}, but limit is ${table_limit}.")
            return profit

        # 3. Spin the Roulette Wheel (18 Red, 18 Black, 1 Green zero)
        # Probability of winning a Red bet is 18/37
        won = random.random() < (18 / 37)
        
        if won:
            profit += bet
            sequence.pop(0)
            if len(sequence) > 0:
                sequence.pop(-1)
            if verbose:
                print(f"  Spin {spins}: WON ${bet}. List is now: {sequence}")
        else:
            profit -= bet
            sequence.append(bet)
            if verbose:
                print(f"  Spin {spins}: LOST ${bet}. List is now: {sequence}")
                
    if verbose:
        print(f"  Success! List cleared in {spins} spins. Final Profit: ${profit}")
        
    return profit

def run_mass_simulation(n):
    """Runs the simulation thousands of times to see the true win rate and total profit."""
    wins = 0
    losses = 0
    total_profit = 0
    worst_loss = 0
    
    for _ in range(n):
        result = play_labouchere(verbose=False)
        total_profit += result  # Accumulate the net total of every game played
        
        if result == 10:
            wins += 1
        else:
            losses += 1
            # Track the most devastating single loss
            if result < worst_loss:
                worst_loss = result

    win_rate = (wins / n) * 100
    print(f"\n--- Results after {n:,} attempts ---")
    print(f"Times you successfully won $10:  {wins:,} ({win_rate:.2f}%)")
    print(f"Times the system FAILED you:     {losses:,}")
    
    if losses > 0:
        print(f"Worst single loss:               ${worst_loss:,.2f}")
        
    print("-" * 40)
    print(f"OVERALL NET PROFIT:              ${total_profit:,.2f}")
    print("-" * 40)

def main():
    print("--- Labouchere Roulette Simulator ---")
    print("Initial List: [1, 2, 3, 4] (Target Profit: $10)")
    print("Assumptions: $1000 Bankroll, $500 Table Limit, European Roulette")
    
    while True:
        print("\nOptions:")
        print("  [1] Watch a single game play out step-by-step")
        print("  [2] Simulate a massive number of games")
        print("  [q] Quit")
        
        choice = input("\nChoose option: ").strip().lower()

        if choice in ("q", "quit", "exit"):
            sys.exit()

        elif choice == "1":
            print("\nStarting a single game...\n")
            play_labouchere(verbose=True)

        elif choice == "2":
            raw = input("How many games to simulate? ").strip()
            try:
                n = int(raw)
            except ValueError:
                print("Error: Please enter a valid number.")
                continue

            if n <= 0:
                print("Error: Number must be at least 1.")
                continue
            if n > 1_000_000:
                print("Error: Let's keep it under 1,000,000 to save time.")
                continue
                
            print(f"\nRunning {n:,} games... please wait.")
            run_mass_simulation(n)

        else:
            print("Invalid option. Please enter 1, 2, or q.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting.")
        sys.exit()