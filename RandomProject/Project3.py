import random

print("Welcome to the Dice Roller!")

# Dictionary containing the ASCII art for each die face
dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
}

# 1. Get user input
num_of_dice = int(input("How many dice do you want to roll? "))  

# 2. Roll the dice and store results in a list
dice_results = []
for _ in range(num_of_dice):
    roll = random.randint(1, 6)
    dice_results.append(roll)

print("\nResult:")

# 3. Print the dice side-by-side
# We loop through each of the 5 rows of the ASCII art
for line in range(5):
    for die in dice_results:
        # Print the current line for each die rolled, followed by a space
        print(dice_art.get(die)[line], end="  ")
    print()  # Move to the next line after all dice in that row are printed

# 4. Calculate and print the total
total = sum(dice_results)
print(f"\nYou rolled: {dice_results}")
print(f"Total: {total}")