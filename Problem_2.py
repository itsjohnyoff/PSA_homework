import random

# note: quick clarification added; logic unchanged

def sim(slots, bullets, spin, trials=100000):
    # simulate the conditional probability of dying given the first pull was a click
    # `slots` is the cylinder size, `bullets` lists indexes with bullets,
    # `spin` boolean indicates whether the cylinder is spun again before the
    # second pull, and `trials` controls Monte Carlo samples.
    deaths = 0
    valid = 0

    for _ in range(trials):
        # randomly pick a starting cylinder position (0..slots-1)
        start = random.randint(0, slots - 1)

        # if there was a bullet at the starting position, you'd have heard a bang
        # so skip those trials — we only want cases where the first pull clicked
        if start in bullets:
            continue

        # this trial matches the observed "click" condition
        valid += 1

        if spin:
            # if the player spins, the next slot is uniformly random again
            next_slot = random.randint(0, slots - 1)
        else:
            # without spinning, the cylinder advances one position deterministically
            next_slot = (start + 1) % slots

        # check if the next trigger pull results in firing a bullet
        if next_slot in bullets:
            deaths += 1

    # return the probability of dying given that the first pull was a click
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
