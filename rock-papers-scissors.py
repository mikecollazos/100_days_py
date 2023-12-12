import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_draw = int((input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")))


computer_draw = random.randint(0, 2)
print(f"computer chose {computer_draw}")

images = [rock, paper, scissors]


if user_draw >= 3 or user_draw < 0:
    print("you typed an invlaid number. Try a number 0-2")
elif user_draw == 0 and computer_draw == 2:
    print("you win!")
    print(images[user_draw] + "\n" + images[computer_draw])
elif user_draw == 2 and computer_draw == 0:
    print("you lose")
    print(images[user_draw] + "\n" + images[computer_draw])
elif computer_draw > user_draw:
    print("you lose")
    print(images[user_draw] + "\n" + images[computer_draw])
elif user_draw > computer_draw:
    print("you win")
    print(images[user_draw] + "\n" + images[computer_draw])
elif computer_draw == user_draw:
    print("It is a draw")
    print(images[user_draw] + "\n" + images[computer_draw])

