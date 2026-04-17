import random

def play_game(verbose=False):
    seq = [1, 2, 3, 4]
    profit = 0
    spins = 0
    bankroll = 1000
    table_limit = 500
    
    while len(seq) > 0:
        spins += 1
        
        if len(seq) == 1:
            bet = seq[0]
        else:
            bet = seq[0] + seq[-1]

        if bet > (bankroll + profit):
            if verbose: 
                print(f"  bankrupt at spin {spins}. needed ${bet}, had ${bankroll + profit}")
            return profit, "bankrupt"
        
        if bet > table_limit:
            if verbose: 
                print(f"  table limit hit at spin {spins}. needed ${bet}")
            return profit, "limit"

        won = random.random() < (18 / 37)
        
        if won:
            profit += bet
            seq.pop(0)
            if len(seq) > 0:
                seq.pop(-1)
            if verbose:
                print(f"  spin {spins}: won ${bet} | list: {seq}")
        else:
            profit -= bet
            seq.append(bet)
            if verbose:
                print(f"  spin {spins}: lost ${bet} | list: {seq}")
                
    if verbose:
        print(f"  success! cleared in {spins} spins. profit: ${profit}")
        
    return profit, "won"

print("--- Labouchere Simulator ---")
print("Target: $10 | Bankroll: $1000 | Limit: $500")

while True:
    print("\n1. Watch one game")
    print("2. Simulate many games")
    print("q. Quit")
    
    choice = input("pick: ").strip().lower()

    if choice in ('q', 'quit', 'exit'):
        break
        
    elif choice == '1':
        print()
        play_game(verbose=True)
        
    elif choice == '2':
        try:
            n = int(input("how many games? "))
            if n <= 0 or n > 1000000:
                print("keep it between 1 and 1,000,000")
                continue
                
            wins = 0
            bankrupts = 0
            limits = 0
            total_profit = 0
            worst = 0
            
            print(f"\nrunning {n} games...")
            for _ in range(n):
                res, status = play_game()
                total_profit += res
                
                if status == "won":
                    wins += 1
                elif status == "bankrupt":
                    bankrupts += 1
                    if res < worst: worst = res
                elif status == "limit":
                    limits += 1
                    if res < worst: worst = res

            win_rate = (wins / n) * 100
            print(f"\n--- results for {n} games ---")
            print(f"won $10:          {wins} times ({win_rate:.1f}%)")
            print(f"bankrupted:       {bankrupts} times")
            print(f"hit table limit:  {limits} times")
            if (bankrupts + limits) > 0:
                print(f"worst loss:       ${worst}")
            print("-" * 30)
            print(f"total net profit: ${total_profit}")
            print("-" * 30)
            
        except ValueError:
            print("invalid number")
            
    else:
        print("bad input")