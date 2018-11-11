import random

def roll_dice():
    a=random.randint(1, 7)
    b=random.randint(1, 7)
    return(a+b)
a="y"
while a=="y":
    guess=input("Guess numbers sum")
    sum=roll_dice()
    if guess==sum:
        print("YOU WIN")
    else:
        print("Sorry you lose the sum={}").format(sum)
    a=input("Do you want to play again? y/n")
