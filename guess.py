import random
def guess():
    name = input("Hi what is Your Name? ")
    chance = 6
    print(f"Nice to meet you {name.capitalize()}. Lets play a game :)")
    print("I will think of a number between 1 and 20 and you have to guess that number :)")
    mynum = random.randint(1, 20)
    while (chance != 0):
        print(f"Chances Left : {chance}")
        g = int(input("Take a guess : "))
        if g > 20:
            print("only numbers between 1 and 20!")
            continue
        if g == mynum:
            print(f"Congragulations {name.capitalize()}! You won, I was thinking of {mynum}")
            break
        elif g < mynum:
            print("Wrong guess :( guess is lower than the number")
        else:
            print("Wrong guess :( guess is higher than the number")
        chance -= 1
    else:
        print(f"Sorry :( The number I was thinking of {mynum}")
    check = input("Do you want to Play Again Y/N : ")
    if not check.isalpha():
        raise ValueError("Input must be a string!")
    if check.lower() == 'y' or check.lower() == 'yes':
        guess()
    print(f"Thanks For Playing {name.capitalize()} :)")


guess()
