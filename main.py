import random

def main():
    number = RandomNumber()
    userInput = int(input("Enter Number between (1-9): "))
    return print(CheckNumbers(number, userInput))

def RandomNumber():
    return None

def CheckNumbers(a,b):
    if a == b:
        return "You WON"    
    else:
        return "You Lost!!"
main()