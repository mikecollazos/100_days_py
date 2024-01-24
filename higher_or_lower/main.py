from art import logo,vs
import random
from game_data import data


def random_dict_item():
    random_item = random.choice(data)
    return random_item


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def main():
    print(logo)
    compare_a_dict = random_dict_item()   
    compare_b_dict = random_dict_item()  

    score = 0
    game_should_continue = True

    while game_should_continue:
        compare_a_dict = compare_b_dict
        compare_b_dict = random_dict_item()
        while compare_a_dict == compare_b_dict:
            compare_b_dict = random_dict_item

        print(f"Compare A: {compare_a_dict['name']}, a {compare_a_dict['description']} from {compare_a_dict['country']}")
        print(vs)
        print(f"Compare B: {compare_b_dict['name']}, a {compare_b_dict['description']} from {compare_b_dict['country']}") 

        response = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        a_followers = compare_a_dict['follower_count']
        b_followers = compare_b_dict['follower_count']
        if check_answer(response, a_followers, b_followers):
            score += 1
            print(f"You Guessed right. Your Current score is {score} \n")
        else:
            print(f"You Guessed wrong. Your Final score is {score} \n")
            game_should_continue = False

main()