import hashlib
import os
import time
import sys

def find_collision(bits=40):
    hex_chars = bits // 4
    seen = {}
    attempts = 0
    start_time = time.time()
    
    print(f"\nTarget: {bits} bits ({hex_chars} hex chars)")
    print("Hashing random inputs...\n")

    while True:
        # mix counter with random bytes for unique inputs
        test_input = f"input_{attempts}_{os.urandom(4).hex()}"
        
        full_hash = hashlib.md5(test_input.encode('utf-8')).hexdigest()
        short_hash = full_hash[:hex_chars]
        attempts += 1
        
        if short_hash in seen:
            if seen[short_hash] != test_input:
                end_time = time.time()
                
                print("\nCOLLISION FOUND !")
                print(f"Time: {end_time - start_time:.2f} seconds")
                print(f"Attempts: {attempts}")
                print("-" * 40)
                print(f"Input 1: {seen[short_hash]}")
                print(f"Input 2: {test_input}")
                print(f"Hash 1: {hashlib.md5(seen[short_hash].encode('utf-8')).hexdigest()}")
                print(f"Hash 2: {full_hash}")
                print(f"Matching part: {short_hash}")
                print("-" * 40 + "\n")
                break
        else:
            seen[short_hash] = test_input
            
        if attempts % 500000 == 0:
            print(f" checked {attempts} hashes...")

def main():
    print("--- MD5 Birthday Attack ---")
    
    while True:
        print("\n[1] Start attack")
        print("[q] Quit")
        
        choice = input("Choice: ").strip().lower()

        if choice in ("q", "quit", "exit"):
            break
        elif choice == "1":
            find_collision(40)
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()