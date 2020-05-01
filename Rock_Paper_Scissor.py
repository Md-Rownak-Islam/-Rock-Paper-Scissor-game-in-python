# -Rock-Paper-Scissor-game-in-python
import random

print("WELCOME TO MY ROCK, PAPER, SCISSOR GAME!! PRESS\n"
      "rock = r \n"
      "paper = p \n"
      "scissor = s \n   "
      "(5 points to win) \n"
      "================================================")

option = ["r", "p", "s"]
com_point = 0
user_point = 0


while user_point <=5 or com_point <=5:
    if user_point ==5:
        print("YOU WIN!!!!!!!!!!!!")
        break
    if  com_point == 5:
        print("YOU LOOSE!!!!!!!!!!!")
        break
    com_guess = random.choice(option)
    user_guess = input("Enter = ")
    if com_guess == "r" and user_guess == "p":
        print("Rock! - You win")
        user_point +=1
        print("Point- ", user_point, "vs", com_point)
    elif com_guess == "p" and user_guess == "s":
        print("Paper! - You win")
        user_point += 1
        print("Point- ", user_point, "vs", com_point)
    elif com_guess == "s" and user_guess == "r":
        print("Scissor  - You win")
        user_point += 1
        print("Point- ", user_point, "vs", com_point)
    elif com_guess == user_guess:
        print ("Tie")
        print("Point- ", user_point, "vs", com_point)
    else:
        print(com_guess, " - You lose")
        com_point +=1
        print("Point- ", user_point, "vs", com_point)

