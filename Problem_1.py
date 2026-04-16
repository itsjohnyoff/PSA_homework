import random

def flip_until_heads():
    j = 1
    while random.random() < 0.5:
        j += 1
    return 2 ** j

def simulate(n):
    total = 0
    for _ in range(n):
        total += flip_until_heads()
    return total / n

def run_sweep():
    sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000]
    results = []
    for n in sizes:
        avg = simulate(n)
        results.append((n, avg))
    return results

def print_sweep(results):
    print("\nGames Played      Average Payout")
    print("-" * 32)
    for n, avg in results:
        print(f"  {n:>10,}        ${avg:>8.2f}")
    print()

def main():
    print("--- St. Petersburg Paradox Simulator ---")

    while True:
        print("\nOptions:")
        print("  [1] Run a sweep (10 to 1,000,000 games)")
        print("  [2] Simulate a specific number of games")
        print("  [q] Quit")

        choice = input("\nChoose option: ").strip().lower()

        if choice in ("q", "quit", "exit"):
            break

        elif choice == "1":
            results = run_sweep()
            print_sweep(results)

        elif choice == "2":
            raw = input("Enter number of games: ").strip()
            try:
                n = int(raw)
            except ValueError:
                print("Error: Please enter a valid number.")
                continue

            if n <= 0:
                print("Error: Number must be at least 1.")
                continue
            if n > 10_000_000:
                print("Error: Number too large (limit: 10,000,000).")
                continue

            print(f"Running {n:,} games...\n")
            avg = simulate(n)
            print("Results:")
            print(f"  Total games:    {n:,}")
            print(f"  Avg payout:     ${avg:,.2f}\n")

        else:
            print("Invalid option. Please enter 1, 2, or q.")

if __name__ == "__main__":
    main()