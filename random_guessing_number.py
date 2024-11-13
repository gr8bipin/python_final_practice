import random

def guess_number():
    """Guessess a random number between 1 and 100."""
    number = random.randint(1, 100)
    guess = 0

    while guess != number:
        guess = int(input("Guess a number between 1 and 100:"))

        if guess < number:
            print("Too low. Guess again.")
        elif guess > number:
            print("Too high. Guess again.")
        else:
            print("Congratulations! You guessed the number.")


if __name__ == "__main__":
    guess_number()