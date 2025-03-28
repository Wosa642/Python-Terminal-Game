import random

def get_random_number():
    # Generate a random number between 1 and 100.
    return random.randint(1, 100)

def play_game():
    attempts_left = 7
    number = get_random_number()

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess the number.")
    print("Good luck!")

    while attempts_left > 0:
        try:
            guess = int(input('Enter your guess: '))
            
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number!")
                break  # Exit the loop if the guess is correct

            # Increment attempts and decrement attempts_left only for incorrect guesses
            
            attempts_left -= 1

            # Check if the player has run out of attempts
            if attempts_left == 0:
                print(f"Sorry, you've used all your attempts. The number was {number}.")
                break

            print(f"You have {attempts_left} attempts left.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print("Game Over!")
    print("Thank you for playing!")
if __name__ == "__main__":
    play_game()