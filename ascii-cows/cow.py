#!/usr/bin/env python3
import os

# cow.py
# ASCII Cows in the command line!
# 
# MIT License
# ©Birdie Works '25


# Get the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
cow_file = os.path.join(script_dir, 'cows.txt')

# Load cows from file
with open(cow_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Split cows by two or more blank lines
cows = [cow.strip() for cow in content.split('\n\n') if cow.strip()]

def show_all():
    for i, cow in enumerate(cows, 1):
        print(f"--- Cow {i} ---")
        print(cow)
        print()

def search_cows(term):
    results = [cow for cow in cows if term.lower() in cow.lower()]
    if results:
        for i, cow in enumerate(results, 1):
            print(f"--- Result {i} ---")
            print(cow)
            print()
    else:
        print("No cows found for that search.")

def main():
    while True:
        print("ASCII Cow Viewer")
        print("1. Browse all cows")
        print("2. Search cows")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            show_all()
        elif choice == '2':
            term = input("Enter search term: ").strip()
            search_cows(term)
        elif choice == '3':
            break
        else:
            print("Invalid choice, try again.")
        input("Press Enter to continue...")  # Pause before showing menu again
        os.system('clear')  # Clear terminal

if __name__ == "__main__":
    main()
