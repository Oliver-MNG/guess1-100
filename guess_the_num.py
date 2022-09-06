import random


print("Welcome to the 'Guess the Number' game!")
print("I am thinking of the number between 1 and 100.")
number = random.randint(1, 100)
difficulty = input("Choose the difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    i = 11
    while i > 0:
        guess = int(input(f"You have {i} attempts remaining to guess the number.\nMake a guess: "))
        if guess == number:
            print(f"Yo maaan you found it, it was {number}")
            i=0
        elif guess > number:
            print('Too high')
        elif guess < number:
            print('Too low')
        i-=1
        if i == 0:
            print(f"You lose the number was {number}")
elif difficulty == 'hard':
    i = 5
    while i > 0:
        guess = int(input(f"You have {i} attempts remaining to guess the number.\nMake a guess: "))
        if guess == number:
            print(f"Yo maaan you found it, it was {number}")
            i = 0
        elif guess > number:
            print('Too high')
        elif guess < number:
            print('Too low')
        i-=1
        if i == 0:
            print(f"You lose the number was {number}")


