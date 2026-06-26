print("Welcome to Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
from random import randint
secret_number = randint(1,100)
tries = 0
guess = 0
while guess != secret_number:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if 1<= guess <= 100:
            tries+=1
        if guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100")
    except ValueError:
        print("Invalid guess")

if guess == secret_number:
    print(f"You guessed it right after {tries} tries")

if tries <= 3:
    print("Amazing! You're a guessing genius!")

elif tries <= 7:
    print("Good job!")

else:
    print("You got it! Keep practicing to improve your score.")

