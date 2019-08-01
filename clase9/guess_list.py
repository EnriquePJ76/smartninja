# -*- coding: utf-8 -*-

import json

try:
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        score_list.sort()
        print("Top scores (attempts): " + str(score_list[:3]))
except:
    print ("No hay puntuaciones guardadas")
    score_list = []


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
        score_list.append(attempts)
        print ("You are the champion!! save your scope")
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")