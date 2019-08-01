import json
import datetime
import random


# Leo el fichero y si no existe inicio score_list como vacío.
try:
    with open("score_data.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        for score_dict in score_list:
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
except:
    print ("No hay puntuaciones guardadas")
    score_list = []

# Optengo el secrect y empieza el juego
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
        data = {
            "attempts": attempts,
            "date": str(datetime.datetime.now())
        }
        score_list.append(data)
        print ("You are the champion!! save your scope")
        with open("score_data.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")