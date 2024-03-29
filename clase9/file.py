# -*- coding: utf-8 -*-
try:
    with open("score.txt", "r") as score_file:
        best_score = int(score_file.read())
        print("Top score (attempts): " + str(best_score))
except:
    print ("No hay puntuaciones guardadas")
    best_score = 100

import random

secret = random.randint(1, 30)
attempts = 0

while True:
    try:
        guess = int(input("Guess the secret number (between 1 and 30): "))
    except:
        print ("Por favor escribe solo números")
        continue

    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        if attempts < best_score:
            print ("You are the champion!! save your scope")
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")