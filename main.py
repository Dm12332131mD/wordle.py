# Wordle.py by DmmD

# Imports
import os
import random

# Configurations
maxTries = 6

# Variables
with open("texts/answers.txt", "r") as file:
    answers = file.read().split("\n")
with open("texts/valid.txt", "r") as file:
    valid = file.read().split("\n")

# Functions
def game():
    guesses, answer = [], random.choice(answers)
    for i in range(maxTries):
        while True:
            render(answer, guesses) 
            print("Enter below a 5-letter word:")
            guess = input("> ")
            if guess in answers or guess in valid:
                guesses.append(guess)
                break
        if guess == answer:
            render(answer, guesses)
            print("You won!")
            input()
            break
    if guess != answer:
        render(answer, guesses)
        print(f"You lost! The word was: {answer}")
        input()

def render(answer, guesses):
    os.system("cls")
    print("=== [ Wordle.py ] ===\n")
    for i in range(len(guesses)):
        guess = guesses[i]
        characters = []
        for j in range(5):
            character = guess[j]
            if character == answer[j]:
                characters.append(f"\033[102m\033[30m {character} \033[0m")
            elif guess.count(character) <= answer.count(character):
                characters.append(f"\033[103m\033[30m {character} \033[0m")
            else:
                characters.append(f"\033[100m\033[37m {character} \033[0m")
        print(" ".join(characters) + "\n")
    for i in range(maxTries - len(guesses)):
        print("\033[100m   \033[0m " * 5 + "\n")

while True:
    game()