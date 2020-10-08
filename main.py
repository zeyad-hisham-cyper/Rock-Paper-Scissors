from random import *
import time
choices = ["Rock", "Paper", "Sicssors"]

computer = choices[randint(0, 2)]

print("welcome in our game")
time.sleep(1)
print("please choose paper, rock or scissors")
time.sleep(1)
print("If you want exit type 'x'")
time.sleep(1)
P_result = 0
C_result = 0

while True:
    player = input("Rock, Paper, Siccors ?")
    if player == computer:
        print(computer)
        print("Tie")
        print("computer: {} - Player: {}".format(C_result, P_result))
        print("-------------------------------")
    elif player == "Rock":
        if computer == "Paper":
            print(computer)
            print("computer Win")
            C_result += 1
            print("computer: {} - Player: {}".format(C_result, P_result))
            print("-------------------------------")
        else:
            print("player Win")
            P_result += 1
            print("computer: {} - Player: {}".format(C_result, P_result))
            print("-------------------------------")
    elif player == "Paper":
        if computer == "Rock":
            print("Player Win")
            P_result += 1
            print("computer: {} - Player: {}".format(C_result, P_result))
            print("-------------------------------")
        else:
            print("Computer Win")
            C_result += 1
            print("computer: {} - Player: {}".format(C_result, P_result))
            print("-------------------------------")

    elif player == "Sicssors":
        if computer == "Rock":
            print("computer Win")
            C_result += 1
            print("computer: {} - Player: {}".format(C_result, P_result))
            print("-------------------------------")
        else:
            print("player Win")
            P_result += 1
            print("computer: {} - Player: {}".format(C_result, P_result))
            print("-------------------------------")
    elif player == "x":
        print("Thank you for your time ^_^")
        break
    else:
        print("Invalid Input")

    computer = choices[randint(0, 2)]
