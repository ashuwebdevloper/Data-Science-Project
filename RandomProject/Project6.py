import random

words = ("apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon")
word = random.choice(words)
print("Welcome to the Word Guessing Game!")


hangman_art = {0 : (" ",
                    " ",
                    " "),
               1 : (" o ",
                    "  ",
                    "  "),
                2 : (" o ",
                    " / ",
                    "  "),
                3 : (" o ",
                    "/| ",
                    "  "),
                4 : (" o ",
                    "/|\\",
                    "  "),
                5 : (" o ",
                    "/|\\",
                    "/  "),
                6 : (" o ",
                    "/|\\",
                    "/ \\"),
                }


def display_hangman(wrong_guesses):
    print("*************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*************")

def display_hint(hint):
    print("Hint: " + " ".join(hint))

def display_answer(answer):
    print("Answer: " + " ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    
    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            if "_" not in hint:
                display_answer(answer)
                print("Congratulations! You've guessed the word!")
                is_running = False  
        else:
            wrong_guesses += 1
            if wrong_guesses == 6:
                display_hangman(wrong_guesses)
                print(f"Game Over! The word was: {answer}")
                is_running = False


if __name__ == "__main__":
    main()