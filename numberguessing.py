import random

secret = random.randint(1, 10)
guess = None
tries = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))
    tries += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print(f"Correct! The number was {secret}. You guessed it in {tries} tries.")