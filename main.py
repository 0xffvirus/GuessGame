import random

def main():
    number = RandomNumber()
    userInput = int(input("Enter Number between (1-9): "))
    return CheckNumbers(number, userInput)

def RandomNumber():
    return random.randint(1,9)

def CheckNumbers(a,b):
    return None    

main()