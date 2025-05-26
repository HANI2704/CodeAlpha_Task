
import random

List = ["google", "code", "template", "python", "task"]

word = random.choice(List)
guessed_letters = []
max_attempts = 6
wrong_attempts = 0

print("Welcome to Hangman!")
print("_ " * len(word))

while wrong_attempts < max_attempts:
    guess = input("Enter a letter: ").lower()
    
   
    guessed_letters.append(guess)

   
    if guess in word:
        print("Good guess!")
    else:
        print("Wrong guess.")
        wrong_attempts += 1

        display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word.strip())
    print(f"Wrong attempts: {wrong_attempts} / {max_attempts}\n")

    if all(letter in guessed_letters for letter in word):
        print("🎉 Congratulations! You guessed the word:", word)
        break
else:
    print("Game Over! The word was:", word)
