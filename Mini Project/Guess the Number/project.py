# python3 ./project.py




import random

target = random.randint(1, 10)

while True:
    userChoice = int(input("Guess the Target : "))
    if(userChoice == target):
        print("You got a Success : Correct Guess!!!")
        break
    elif(userChoice < target):
        print("Your number is small. Take a bigger Guess.")
    else:
        print("Your number is big. Take a small Guess.")

print("------GAME OVER------")