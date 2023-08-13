from helper_variables import GUESSES


def get_num_lives() -> int:
    """Asks user input and returns an integer representing the number of guesses the player will get in the game"""
    while True:
        level = input("Please enter 'easy' or 'hard': ").lower()
        if level not in ("easy", "hard"):
            print("Sorry, that's not an acceptable level. Please try again!")
        else:
            num_lives = 10 if level == "easy" else 5
            return num_lives


def get_guess() -> int:
    """Asks user input and returns the integer representing the player's guess"""
    while True:
        guess = input("What is your guess: ")
        if not guess.isnumeric():
            print("That's not a valid number. Please try again.")
        else:
            return int(guess)


def is_guess_valid(guess: int) -> bool:
    """Takes in the player's guess, checks if its validity and returns a Boolean to that effect"""
    if guess < 1 or guess > 100:
        print("That's not a valid guess. Please enter a number between 1 and 100.")
        return False
    if guess in GUESSES:
        print("You already guessed that, silly. Try another number now.")
        return False
    return True


def check_guess(num: int, guess: int) -> bool:
    """Takes in two integers (a random number and the player's guess)
    and returns a Boolean value, True if the integers are equal, False otherwise"""
    if guess == num:
        return True
    elif guess > num:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    return False


def restart_game() -> bool:
    """Asks user input representing, checks for its validity, returns a Boolean"""
    while True:
        restart = input("Would you like to play again? Please enter 'yes' or 'no'? ").lower()
        if restart not in ("yes", "no"):
            print("That's not a valid input. Please try again.")
        elif restart == "yes":
            print("Great! Let's start over!")
            return True
        else:
            print("All right. See you next time!")
            return False
