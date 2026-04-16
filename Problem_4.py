import random
import sys

def play_oscars_grind(spins_to_play, verbose=False, bankroll=1000, table_limit=500):
    """Simulates a session of Oscar's Grind for a specific number of spins."""
    total_profit = 0
    sequence_profit = 0
    bet = 1
    max_bet_reached = 1
    worst_drawdown = 0

    for spin in range(1, spins_to_play + 1):
        # 1. Check Reality Limits (Bankroll and Table Limit)
        if bet > (bankroll + total_profit):
            if verbose:
                print(f"  [!] BANKRUPT at spin {spin}. Needed ${bet}, but only had ${bankroll + total_profit}.")
            return total_profit, max_bet_reached, worst_drawdown, "Bankrupt"

        if bet > table_limit:
            if verbose:
                print(f"  [!] TABLE LIMIT REACHED at spin {spin}. Needed ${bet}, limit is ${table_limit}.")
            return total_profit, max_bet_reached, worst_drawdown, "Table Limit"

        # Track the highest bet we were forced to make
        if bet > max_bet_reached:
            max_bet_reached = bet

        # 2. Spin the Roulette Wheel (Betting Black: 18/37 chance)
        won = random.random() < (18 / 37)

        if won:
            total_profit += bet
            sequence_profit += bet
            if verbose:
                print(f"  Spin {spin:<4}: WON  ${bet:<4} | Seq Profit: ${sequence_profit:<4} | Total: ${total_profit}")

            # If we hit our +1 sequence goal, pocket it and reset!
            if sequence_profit >= 1:
                sequence_profit = 0
                bet = 1  
            else:
                # Increase bet by 1, UNLESS it pushes us over the +1 sequence profit goal
                next_bet = bet + 1
                if sequence_profit + next_bet > 1:
                    bet = 1 - sequence_profit
                else:
                    bet = next_bet
        else:
            total_profit -= bet
            sequence_profit -= bet
            if verbose:
                print(f"  Spin {spin:<4}: LOST ${bet:<4} | Seq Profit: ${sequence_profit:<4} | Total: ${total_profit}")
            # IMPORTANT: On a loss, the bet size stays exactly the same.

        # Track how much money we are losing at our lowest point
        if total_profit < worst_drawdown:
            worst_drawdown = total_profit

    if verbose:
        print(f"\n  Finished {spins_to_play} spins. Final Profit: ${total_profit}")

    return total_profit, max_bet_reached, worst_drawdown, "Completed"

def run_mass_simulation(spins_per_session, num_sessions, bankroll=1000, table_limit=500):
    """Runs the simulation thousands of times to prove the strategy fails in the long run."""
    successes = 0
    stuck_in_negative = 0  # Catches games that run out of time while losing
    bankruptcies = 0
    limit_hits = 0
    total_net_profit = 0
    absolute_worst_drawdown = 0
    absolute_max_bet = 0

    for _ in range(num_sessions):
        profit, max_bet, worst_drawdown, status = play_oscars_grind(
            spins_to_play=spins_per_session,
            verbose=False,
            bankroll=bankroll,
            table_limit=table_limit
        )

        total_net_profit += profit

        if max_bet > absolute_max_bet:
            absolute_max_bet = max_bet
        if worst_drawdown < absolute_worst_drawdown:
            absolute_worst_drawdown = worst_drawdown

        if status == "Completed" and profit > 0:
            successes += 1
        elif status == "Completed" and profit <= 0:
            stuck_in_negative += 1
        elif status == "Bankrupt":
            bankruptcies += 1
        elif status == "Table Limit":
            limit_hits += 1

    print(f"\n--- Results after {num_sessions:,} sessions ({spins_per_session:,} spins each) ---")
    print(f"Sessions that survived in profit:   {successes:,}")
    print(f"Sessions stuck in negative profit:  {stuck_in_negative:,}")
    print(f"Sessions BANKRUPTED:                {bankruptcies:,}")
    print(f"Sessions hitting TABLE LIMIT:       {limit_hits:,}")
    print("-" * 55)
    print(f"Highest single bet placed:        ${absolute_max_bet:,}")
    print(f"Worst financial drop (drawdown):  ${absolute_worst_drawdown:,.2f}")
    print(f"OVERALL NET PROFIT (All sessions):${total_net_profit:,.2f}")
    print("-" * 55)

def main():
    print("--- Oscar's Grind Strategy Simulator ---")
    print("Target: +1 Unit per sequence")
    print("Assumptions: $1000 Bankroll, $500 Table Limit, European Roulette")
    
    while True:
        print("\nOptions:")
        print("  [1] Watch a single 50-spin session step-by-step")
        print("  [2] Simulate massive scale")
        print("  [q] Quit")
        
        choice = input("\nChoose option: ").strip().lower()

        if choice in ("q", "quit", "exit"):
            sys.exit()

        elif choice == "1":
            print("\nStarting a single 50-spin session...\n")
            play_oscars_grind(spins_to_play=50, verbose=True)

        elif choice == "2":
            raw_sessions = input("How many full sessions to simulate? ").strip()
            raw_spins = input("How many spins per session? ").strip()
            try:
                num_sessions = int(raw_sessions)
                num_spins = int(raw_spins)
            except ValueError:
                print("Error: Please enter valid numbers.")
                continue

            if num_sessions <= 0 or num_spins <= 0:
                print("Error: Numbers must be at least 1.")
                continue
                
            print(f"\nRunning {num_sessions:,} sessions... please wait.")
            run_mass_simulation(spins_per_session=num_spins, num_sessions=num_sessions)

        else:
            print("Invalid option. Please enter 1, 2, or q.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting.")
        sys.exit()