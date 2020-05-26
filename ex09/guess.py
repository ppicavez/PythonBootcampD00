from random import randrange


def try_to_guess():
    initialisation = (
        "This is an interactive guessing game!\n"
        "You have to enter a number between 1 and 99 to "
        "find out the secret number.\n"
        "Type 'exit' to end the game.\n"
        "Good luck!"
    )
    guess = "What's your guess between 1 and 99?\n"
    douglas_adams_ref = (
        "The answer to the ultimate question of life, "
        "the universe and everything is 42.\n"
    )
    first_try = "Congratulations! You got it on your first try!\n"
    secret_number = randrange(1, 100)
    nb_trial = 0
    print(initialisation)

    while True:
        answer = input(guess)
        if answer.lower() == "exit":
            print("Goodbye!")
            break

        if not answer.isdigit():
            print("That's not a number.")
            continue
        user_trial = int(answer)
        if (user_trial < 0) or (user_trial > 100):
            print("Incorrect number.")
            continue
        # got the good input here
        nb_trial = nb_trial + 1
        if user_trial == secret_number:
            if nb_trial == 1:
                print(first_try)
            if secret_number == 42:
                print(dadams_ref)
            print("Congratulations, you ve'got it!")
            if nb_trial != 1:
                print(f"You won in {nb_trial} attempts!")
            break
        elif user_trial > secret_number:
            print("Too high!")
        elif user_trial < secret_number:
            print("Too low!")


if __name__ == "__main__":
    try_to_guess()
