import random

# Function to roll dice if the user wants to roll more than one die
def roll_dice(number_of_dice):
    print("\n🎲 Rolling Dice...\n")

    total = 0

    for i in range(number_of_dice):
        value = random.randint(1, 6)
        total += value
        print(f"Dice {i + 1}: {value}")

    print("------------------------")
    print(f"Total = {total}")
    print("------------------------")


# Main Program when the user runs the program
print("  1  2  3  4  5  6")
print("   DICE ROLLER")
print("  6  5  4  3  2  1")

while True:

    try:
        dice = int(input("\nHow many dice do you want to roll? "))

        if dice <= 0:
            print("Please enter a number greater than 0.")
            continue

        roll_dice(dice)

        choice = input("\nRoll again? (Y/N): ").strip().upper()

        if choice != "Y":
            print("\nThank you for using Dice Roller!")
            break

    except ValueError:
        print("Please enter a valid number.")
