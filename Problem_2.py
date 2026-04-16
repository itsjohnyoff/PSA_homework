import random

def simulate_roulette(slots, bullet_positions, spin_after, trials=100_000):
    deaths = 0
    valid_games = 0  

    for _ in range(trials):
        start = random.randint(0, slots - 1)

        if start in bullet_positions:
            continue
        
        valid_games += 1

        if spin_after:
            next_slot = random.randint(0, slots - 1)
        else:
            next_slot = (start + 1) % slots

        if next_slot in bullet_positions:
            deaths += 1

    return deaths / valid_games

def run_all():
    configs = [
        (6, {0, 1}, "6 slots, adjacent    "),
        (6, {0, 2}, "6 slots, not adjacent"),
        (5, {0, 1}, "5 slots, adjacent    "),
        (5, {0, 2}, "5 slots, not adjacent"),
    ]

    print(f"\n{'Scenario':<26}  {'No Spin (Die %)':<18} {'Spin (Die %)':<18}  Best Choice")
    print("-" * 75)

    for slots, bullets, label in configs:
        p_no_spin = simulate_roulette(slots, bullets, spin_after=False)
        p_spin    = simulate_roulette(slots, bullets, spin_after=True)

        better = "DON'T SPIN" if p_no_spin < p_spin else "SPIN"
        print(f"{label}   {p_no_spin*100:>6.2f}%               {p_spin*100:>6.2f}%               {better}")
        
    print("\nLower % means a better chance of survival.")

def main():
    print("--- Russian Roulette Probability Simulator ---")
    
    while True:
        print("\nOptions:")
        print("  [1] Run the simulation for all 8 scenarios")
        print("  [q] Quit")
        
        choice = input("\nChoose option: ").strip().lower()

        if choice in ("q", "quit", "exit"):
            break

        elif choice == "1":
            run_all()

        else:
            print("Invalid option. Please enter 1 or q.")

if __name__ == "__main__":
    main()