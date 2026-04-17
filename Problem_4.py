import random

def play_game(spins, verbose=False):
    profit = 0
    seq_profit = 0
    bet = 1
    max_bet = 1
    worst = 0
    bankroll = 1000
    limit = 500

    for spin in range(1, spins + 1):
        if bet > (bankroll + profit):
            if verbose: 
                print(f"  bankrupt at spin {spin}. needed ${bet}")
            return profit, max_bet, worst, "bankrupt"

        if bet > limit:
            if verbose: 
                print(f"  table limit hit at spin {spin}. needed ${bet}")
            return profit, max_bet, worst, "limit"

        if bet > max_bet:
            max_bet = bet

        won = random.random() < (18 / 37)

        if won:
            profit += bet
            seq_profit += bet
            if verbose:
                print(f"  spin {spin}: won ${bet} | seq: ${seq_profit} | total: ${profit}")

            if seq_profit >= 1:
                seq_profit = 0
                bet = 1  
            else:
                next_bet = bet + 1
                if seq_profit + next_bet > 1:
                    bet = 1 - seq_profit
                else:
                    bet = next_bet
        else:
            profit -= bet
            seq_profit -= bet
            if verbose:
                print(f"  spin {spin}: lost ${bet} | seq: ${seq_profit} | total: ${profit}")

        if profit < worst:
            worst = profit

    if verbose:
        print(f"\n  finished {spins} spins. final profit: ${profit}")

    return profit, max_bet, worst, "done"

print("--- Oscar's Grind Simulator ---")
print("Target: +1 | Bankroll: $1000 | Limit: $500")

while True:
    print("\n1. Watch a 50-spin session")
    print("2. Simulate many sessions")
    print("q. Quit")
    
    choice = input("pick: ").strip().lower()

    if choice in ('q', 'quit', 'exit'):
        break
        
    elif choice == '1':
        print()
        play_game(50, verbose=True)
        
    elif choice == '2':
        try:
            num_sessions = int(input("how many sessions? "))
            spins = int(input("spins per session? "))
            
            if num_sessions <= 0 or spins <= 0:
                print("must be at least 1")
                continue
                
            print(f"\nrunning {num_sessions} sessions...")
            
            good = 0
            stuck = 0
            bankrupts = 0
            limits = 0
            total_net = 0
            abs_worst = 0
            abs_max_bet = 0
            
            for _ in range(num_sessions):
                p, m_bet, w, status = play_game(spins)
                total_net += p
                
                if m_bet > abs_max_bet: abs_max_bet = m_bet
                if w < abs_worst: abs_worst = w
                
                if status == "done" and p > 0:
                    good += 1
                elif status == "done" and p <= 0:
                    stuck += 1
                elif status == "bankrupt":
                    bankrupts += 1
                elif status == "limit":
                    limits += 1

            print(f"\n--- results for {num_sessions} sessions ({spins} spins each) ---")
            print(f"survived in profit: {good}")
            print(f"stuck in negative:  {stuck}")
            print(f"bankrupted:         {bankrupts}")
            print(f"hit table limit:    {limits}")
            print("-" * 40)
            print(f"highest bet placed: ${abs_max_bet}")
            print(f"worst drop:         ${abs_worst}")
            print(f"overall net profit: ${total_net}")
            print("-" * 40)
            
        except ValueError:
            print("invalid number")
            
    else:
        print("bad input")