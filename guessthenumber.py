
import random

number = random.randint(1, 10)
tries = 1


uname  = input("Hello, What is your username?")

print("Hello", uname + ".", )

question = input("Would you like to play a game? [Y/N] ")
if question == "n":
    print("oh..okey")

if question =="y":
    print("I'm thinking of a number between 1 & 10, Guess within 3 tries")
    guess = int(input("Have a guess: "))
    if guess > number:
        print("Guess lower...")
    if guess < number:
        print("Guess higher...")
    while guess != number:
        tries += 1
        guess = int(input("Try again: "))
        if guess > number:
            print("Guess Lower")
        if guess < number:
            print("Guess Higher")
        if tries == 3:
            break

    if guess == number:
        print("You're right! you win! The number was", number, \
              "and it only", tries, "tries!")
    if guess != number:
        print("Sorry, You lost.")
