questions = ("How many continents are there?",
             "What is the capital of India?",
             "What is the currency of Japan?",
             "What is the largest mammal?", 
             "Who is the current president of the United States?")

options = (("A. 5", "B. 6", "C. 7", "D. 8"),
           ("A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"),
           ("A. Yen", "B. Won", "C. Yuan", "D. Ringgit"),
           ("A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Lion"),
           ("A. Joe Biden", "B. Donald Trump", "C. Barack Obama", "D. George Washington"))

answers = ("C", "B", "A", "B", "B") # Updated for 2026
guesses = []
score = 0

# i will automatically be 0, 1, 2, 3, 4
for i, question in enumerate(questions):
    print("-----------------------------")
    print(f"Question {i+1}: {question}")
    
    # Use i to get the correct options for this question
    for option in options[i]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    # Use i to check against the correct answer
    if guess == answers[i]:
        score += 1
        print("CORRECT!")
    else:
        print(f"INCORRECT! The correct answer was {answers[i]}")

print("-----------------------------")
print(f"FINAL SCORE: {score}/{len(questions)}")
print("-----------------------------")

print("Correct Answers: ", end="")
for answer in answers:  
    print(answer, end=" ")
print()

print("Your Guesses: ", end="")
for guess in guesses:  
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
print("-----------------------------")

