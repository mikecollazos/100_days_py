import random
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = """
  ▄████  █    ██ ▓█████   ██████   ██████    ▄▄▄█████▓ ██░ ██ ▓█████     ███▄    █  █    ██  ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
 ██▒ ▀█▒ ██  ▓██▒▓█   ▀ ▒██    ▒ ▒██    ▒    ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀     ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▓██  ▒██░▒███   ░ ▓██▄   ░ ▓██▄      ▒ ▓██░ ▒░▒██▀▀██░▒███      ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
░▓█  ██▓▓▓█  ░██░▒▓█  ▄   ▒   ██▒  ▒   ██▒   ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒▒▒█████▓ ░▒████▒▒██████▒▒▒██████▒▒     ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
 ░▒   ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░     ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░ ░░▒░ ░ ░  ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░       ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
░ ░   ░  ░░░ ░ ░    ░   ░  ░  ░  ░  ░  ░       ░       ░  ░░ ░   ░         ░   ░ ░  ░░░ ░ ░ ░      ░    ░    ░    ░     ░░   ░ 
      ░    ░        ░  ░      ░        ░               ░  ░  ░   ░  ░            ░    ░            ░    ░         ░  ░   ░     
                                                                                                             ░  
      """


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def difficulty():
    mode = input("choose a difficulty. Type 'easy' or 'hard':  ")
    if mode == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("\nWelcome to the Number Guessing Game! \nI\'m thinking of a number between 1 and 100.") 
    number = random.randint(1,100)
    remaining_turns = difficulty()
    while remaining_turns > 0:
        guess = input("Make a guess: ")
        guess = int(guess)
        if guess == number:
            print(f"You guess right. The number {str(number)}")
            break
        elif guess > number:
            print("Too high. \nGuess again ")
        elif guess < number:
            print("Too low. \nGuess again ")
        remaining_turns -= 1
        print(f"You have {str(remaining_turns)} attempts remaining to guess the number \n")
        if remaining_turns == 0:
            print(f"You have ran out of guesses. The correct number was {str(number)}")
            break

game()




