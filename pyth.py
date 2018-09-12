import random

answer = random.randint(1, 10)
print("Please guess a number between 1-10: ")
guess = int(input())
numberOfGuesses = 0

while guess != answer:
    numberOfGuesses+=1
    if guess > answer:
        print("You guessed too high and answer was {0}".format(answer))
        answer = random.randint(1, 10)
        print("Please guess a number between 1-10: ")
        guess = int(input())
    elif guess < answer:
        print("You guessed too low answer was {}".format(answer))
        answer = random.randint(1, 10)
        "Please guess a number between 1-10: "
        guess = int(input())
    elif guess == answer:
        break


print("You guessed it right answer was {} and number of guesses made was {}".format(answer, numberOfGuesses))

