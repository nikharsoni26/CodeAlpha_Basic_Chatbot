import random

def play_hangman():
    words = ["python", "computer", "programming", "developer", "keyboard"]

    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("==============================")
    print("     WELCOME TO HANGMAN!")
    print("==============================")
    print("Guess the secret word one letter at a time.")
    print("You have", attempts, "wrong attempts available.")

    while attempts > 0:
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Guessed letters:", guessed_letters)
        print("Remaining attempts:", attempts)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word:", secret_word)
            print("You Win!")
            break

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

    else:
        print("\nGame Over!")
        print("The secret word was:", secret_word)


if __name__ == "__main__":
    play_hangman()