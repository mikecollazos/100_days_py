import random
from hangman_words import word_list
from hangman_art import stages, logo

#Generate Random word

#word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


print(f'Pssst, the solution is {chosen_word}.')


#generate blanks
display = []
for i in range(0, len(chosen_word)):
    display += "_"

print(display)

# User begins to guess letter and will check if correct or not.

chosen_word = list(chosen_word)
lives = 6 
print(logo)
while chosen_word != display:
    guess = str(input("Guess a letter:   ").lower())
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])

    print(display)
    if "_" not in display:
        print("You win.")
    if lives == 0:
        print("You lost. No more guesses left")
        break

print(display)