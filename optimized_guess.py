import random
from art_guess import logo


def check_num(guess,number):
    if guess > number:
        print('Too high')
    elif guess < number:
        print('Too low')
    elif guess == number:
        print('Yoo maaaan you got it right!')

print(logo)
print("Welcome to the guessing game!")
print("Now I will guess the number from 1 to 100, and you should find it.")

answer = random.randint(1,101)

difficulty = input("In which difficulty you want to play? Type 'easy' or 'hard': ")

if difficulty == 'easy':
    times = 10
else:
    times = 5

while times > 0:
    guess = int(input("Make a guess: "))
    check_num(guess,answer)
    if guess != answer:
        times -= 1
        print(f"You have {times} lives left.")
    elif guess == answer:
        times = 0




