import random

def guessingGame():

    guessesTaken = 0

    name = input("Enter your name: ")

    number = random.randint(1, 100)

    print(f"Well {name} I think of a number between 1 and 20")

    for guessesTaken in range(6):
        print("Take a guess.")
        guess = int(input("Enter guess: "))

        if guess < number:
            print("Your guess is too low")

        if guess > number:
            print("Your guess is too high")

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken + 1)
        print(f"Good job! {name} Your guessed my number in {guessesTaken} guesses.")

    if guess != number:
        number = str(number)
        print(f"Nah the number I was thinking of is {number}.")

guessingGame()