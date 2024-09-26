import random
from art import logo


def game():
    print(logo)
    replay = "yes"
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    while replay.lower() == "yes":
        answer = random.randint(1, 100)

        set_difficulty = input("\nPlease select a difficulty by typing 'easy' or 'hard': ")
        if set_difficulty.lower() != "easy" and set_difficulty.lower() != "hard":
            print("No such option, please select 'easy' or hard'.")
            continue

        def chosen_difficulty(difficulty):
            if difficulty.lower() == "easy":
                return 10
            else:
                return 5

        attempts_left = chosen_difficulty(set_difficulty)

        while attempts_left > 0:
            print(f"You have {attempts_left} attempts remaining to guess the number.")
            user_guess = input("Make a guess: ")

            try:
                user_guess = int(user_guess)
                if user_guess < 1 or user_guess > 100:
                    print("\nPlease type a numeric answer from 1 to 100.")
                    continue
            except ValueError:
                print("\nPlease type a numeric answer.")
                continue

            attempts_left -= 1

            if user_guess == answer:
                print(f"\nThe answer is {answer}! You win!")
                break
            elif user_guess > answer:
                print(f"\n{user_guess} is too high. test {answer}")
            else:
                print(f"\n{user_guess} is too low.")

            if attempts_left == 0 and user_guess != answer:
                print(f"You've run out of guesses, you lose.\nThe answer was {answer}.")

        replay = input("\nWould you like to play again? Please type 'yes' or 'no': ")


game()
