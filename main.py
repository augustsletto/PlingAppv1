import random
import datetime as dt


f = open("challenges.txt", "r", encoding="UTF-8")

challenges = f.readlines()

players = ["Emma", "Gustav", "August"]

def get_random_player():
    return random.choice(players)

def get_random_challenge():
    return random.choice(challenges)

active_player = get_random_player()


active_challenge = get_random_challenge()



def game_message():
    return f"{active_player}: {active_challenge}"

print(game_message())

def send_notification():
    