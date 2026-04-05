import random

def sim(slots, bullets, spin, trials=100000):
    # simulate chance of dying after hearing a click
    # slots: cylinder size, bullets: bullet indexes, spin: whether to spin again
    deaths = 0
    valid = 0

    for _ in range(trials):
        # pick a random starting position; skip if it was a bullet (we heard a bang)
        start = random.randint(0, slots - 1)
        if start in bullets:
            continue
        valid += 1

        if spin:
            # spinning: next slot is random
            next_slot = random.randint(0, slots - 1)
        else:
            # no spin: next slot is the following chamber
            next_slot = (start + 1) % slots

        # check if the next trigger pull results in firing a bullet
        if next_slot in bullets:
            deaths += 1

    # return estimated conditional probability
    return deaths / valid

print("--- Russian Roulette Sim ---")

# main menu loop
while True:
    print("\n1. Run all scenarios")
    print("q. Quit")
    
    choice = input("pick: ").strip().lower()

    if choice in ('q', 'quit', 'exit'):
        break
        
    elif choice == '1':
        # define different gun configurations: (total slots, bullet positions, display label)
        configs = [
            (6, [0, 1], "6 slots adj    "),
            (6, [0, 2], "6 slots not adj"),
            (5, [0, 1], "5 slots adj    "),
            (5, [0, 2], "5 slots not adj"),
        ]
        
        print("\nscenario        | no spin | spin  | best choice")
        print("-" * 50)
        
        for slots, bullets, label in configs:
            # calculate death probabilities for both choices
            p_no = sim(slots, bullets, False)
            p_spin = sim(slots, bullets, True)
            
            # determine the safest strategy
            better = "dont spin" if p_no < p_spin else "spin"
            print(f"{label} | {p_no*100:.1f}%   | {p_spin*100:.1f}% | {better}")
            
    else:
        print("bad input")
