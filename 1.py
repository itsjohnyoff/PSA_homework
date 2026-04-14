import random
import sys

def play_single_game():
    """Simulates a single game of flipping a coin until it lands on heads."""
    toss_count = 1
    # random.choice([True, False]) simulates a coin flip. True = Heads, False = Tails.
    while random.choice([True, False]) == False: 
        toss_count += 1
    
    # Payout is 2 to the power of the toss count
    return 2 ** toss_count

def main():
    print("--- St. Petersburg Paradox Simulator ---")
    print("Game Rules: A coin is flipped until it lands on Heads.")
    print("Payout: $2^j where j is the number of tosses.")
    print("----------------------------------------")

    while True:
        try:
            # 1. Ask for input
            user_input = input("\nEnter the number of games to simulate (or 'q' to quit): ").strip()
            
            # Allow the user to exit cleanly
            if user_input.lower() in ['q', 'quit', 'exit']:
                print("Exiting simulator. Have a great day!")
                sys.exit()

            # 2. Try to convert to an integer
            num_games = int(user_input)

            # 3. Handle negative numbers and zero
            if num_games <= 0:
                print("Error: You must play at least 1 game. Try again.")
                continue
            
            # 4. Handle massive numbers that would freeze a standard laptop
            if num_games > 10_000_000:
                print("Error: That number is too large and will freeze your computer.")
                print("Please enter a number smaller than 10,000,000.")
                continue

            # 5. Run the simulation
            print(f"Simulating {num_games:,} games... please wait.")
            total_payout = 0
            
            for _ in range(num_games):
                total_payout += play_single_game()
                
            average_payout = total_payout / num_games
            
            # 6. Display results
            print(f">>> Total Payout for all games: ${total_payout:,}")
            print(f">>> Average Payout per game: ${average_payout:,.2f}")

        except ValueError:
            # This catches if they type "hello", "five", or "10.5"
            print("Error: Invalid input! Please enter a whole number (e.g., 100, 1000).")
        except KeyboardInterrupt:
            # This catches if they press Ctrl+C to force quit
            print("\nSimulation interrupted by user. Exiting.")
            sys.exit()

if __name__ == "__main__":
    main()   