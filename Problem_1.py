import random

def play_game():
    # flip until we get tails (50% chance), counting total flips
    flips = 1
    while random.random() < 0.5:
        flips += 1
    # payout doubles with each flip
    return 2 ** flips

def simulate(n):
    # run N games and get the average payout
    total = 0
    for _ in range(n):
        total += play_game()
    return total / n

print("--- St. Petersburg Paradox ---")

# main menu loop
while True:
    print("\n1. Run sweep (10 to 1M)")
    print("2. Custom games")
    print("q. Quit")
    
    choice = input("pick: ").strip().lower()

    if choice in ('q', 'quit', 'exit'):
        break
        
    elif choice == '1':
        # test predefined sizes to see how average grows
        sizes = [10, 100, 1000, 10000, 100000, 1000000]
        print("\nGames  -->  Avg Payout")
        print("------------------------")
        for n in sizes:
            print(f"{n}  -->  ${simulate(n):.2f}")
            
    elif choice == '2':
        try:
            n = int(input("how many games? "))
            # cap at 50M so the script doesn't hang
            if 0 < n <= 50000000:
                print(f"running {n} games...")
                print(f"avg payout: ${simulate(n):.2f}")
            else:
                print("keep it between 1 and 50M")
        except ValueError:
            print("invalid number")
            
    else:
        print("bad input")
