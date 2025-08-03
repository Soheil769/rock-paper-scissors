import sys
import random
your_input=input("please enter a number:\n1:rock\n2:paper\n3:scissors\n")
if your_input.isdigit():
    your_choice=int(your_input)
else:
    print("You must enter a number")
    sys.exit()
if your_choice <0 or your_choice >3 :
    print("You must enter 1 or 2 or 3")
    sys.exit()
else:
    computer_choice=random.choice("123")
    computer_answer=int(computer_choice)
    print("Your choice is " + your_input + "\nComputer choice is " + computer_choice)
if your_choice == 1 and computer_answer == 3:
    print("You won!")
elif your_choice == 2 and computer_answer == 1:
    print("You won!")
elif your_choice == 3 and computer_answer == 2:
    print("You won!")
elif your_choice == computer_answer:
    print("Tie game")
else:
    print("Computer won:(")