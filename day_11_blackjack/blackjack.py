from logo import logo
import random
import os



############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def deal_card():
    card = random.choice(cards)
    return card

# Deal the user and computer 2 cards each
user_cards = []
computer_cards = []

for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

#get user and computer scores
def calculate_scores(card_list):
    if sum(card_list) == 21:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        index = card_list.index(11)
        card_list[index] = 1
    return sum(card_list)

#if comp_score == 0 or user_score == 0: #or user_score > 21:

user_score= calculate_scores(user_cards)
comp_score= calculate_scores(computer_cards)

def play_game():
    is_game_over = False
    while not is_game_over:
        user_score= calculate_scores(user_cards)
        comp_score= calculate_scores(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        if user_cards == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            draw_again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if draw_again == 'y':
                user_cards.append(deal_card())
                user_score=calculate_scores(user_cards)
            else:
                is_game_over = True


    while comp_score < 17:
        computer_cards.append(deal_card())
        comp_score= calculate_scores(computer_cards)


    def compare(user_score, comp_score):
        if user_score > 21 and comp_score > 21:
            return "You went over. You lose 😤"
        if user_score == comp_score:
            return "Draw 🙃"
        elif comp_score == 0:
            return "You Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "You Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif comp_score > 21:
            return "Opponent went over. You win 😁"
        elif user_score > comp_score:
            return "You win 😃"
        else:
            return "You lose 😤"


    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))

print(logo)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('cls' if os.name == 'nt' else 'clear')
  print(logo)
  play_game()

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and comp_score. 
#If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. 
#If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. 
#If the comp_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
