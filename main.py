from art import logo
from helper_functions import get_num_lives, get_guess, is_guess_valid, check_guess, restart_game
from helper_variables import GUESSES
from random import randint

GAME_IN_PROGRESS = True


def play_game() -> None:
    """A game where the computer chooses a random number and
    the player tries to guess it before the number of guesses run out"""
    print(logo)
    print("Hi, there! Before we start please choose a difficulty level.")
    num_lives = get_num_lives()
    print(f"Great! You get {num_lives} guesses.")
    random_num = randint(1, 100)
    print("I'm thinking of a number between 1 and 100. Please guess the number your guesses run out.")
    print(random_num)
    while True:
        guess = get_guess()
        guess_validity = is_guess_valid(guess)
        if guess_validity:
            num_lives -= 1
            GUESSES.append(guess)
        is_guess_true = check_guess(random_num, guess)
        if num_lives > 0 or not is_guess_true:
            print(f"You have {num_lives} guesses left.")
        if num_lives == 0 or is_guess_true:
            if num_lives == 0:
                print("Sorry, you lose! You don't have any guesses left.")
            if is_guess_true:
                print("Congratulations, you won!")
            restart = restart_game()
            if not restart:
                global GAME_IN_PROGRESS
                GAME_IN_PROGRESS = False
            GUESSES.clear()
            break


while GAME_IN_PROGRESS:
    play_game()

