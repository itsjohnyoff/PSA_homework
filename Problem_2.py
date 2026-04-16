import random

def sim(slots, bullets, spin, trials=100000):
    deaths = 0
    valid = 0

    for _ in range(trials):
        start = random.randint(0, slots - 1)
        
        # skip if we died on the first click
        if start in bullets:
            continue
            
        valid += 1

        if spin:
            next_slot = random.randint(0, slots - 1)
        else:
            next_slot = (start + 1) % slots

        if next_slot in bullets:
            deaths += 1

    return deaths / valid

print("--- Russian Roulette Sim ---")

while True:
    print("\n1. Run all scenarios")
    print("q. Quit")
    
    choice = input("pick: ").strip().lower()

    if choice in ('q', 'quit', 'exit'):
        break
        
    elif choice == '1':
        configs = [
            (6, [0, 1], "6 slots adj    "),
            (6, [0, 2], "6 slots not adj"),
            (5, [0, 1], "5 slots adj    "),
            (5, [0, 2], "5 slots not adj"),
        ]
        
        print("\nscenario        | no spin | spin  | best choice")
        print("-" * 50)
        
        for slots, bullets, label in configs:
            p_no = sim(slots, bullets, False)
            p_spin = sim(slots, bullets, True)
            
            better = "dont spin" if p_no < p_spin else "spin"
            print(f"{label} | {p_no*100:.1f}%   | {p_spin*100:.1f}% | {better}")
            
    else:
        print("bad input")