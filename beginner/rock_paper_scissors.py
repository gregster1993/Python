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

images = [rock, paper, scissors]
pc_choice = random.randint(0, 2)
human_choice = int(input("What do you choose? Type O for Rock, 1 for Paper or 2 for Scissors. \n"))

print("You chose: \n",images[human_choice])
print("Computer chose: \n",images[pc_choice])

if human_choice >= 3 or human_choice < 0:
    print("You typed an invalid number. You lose!")
elif human_choice == 0 and pc_choice == 2:
    print("You win!")
elif pc_choice == 0 and human_choice == 2:
    print("You lose!")
elif pc_choice > human_choice:
    print("You lose!")
elif human_choice > pc_choice:
    print("You win!")
elif pc_choice == human_choice:
    print("It's a draw!")
