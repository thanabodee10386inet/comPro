import random

HEADS = 1
TAILS = 2
TOSSES = 5

def toss():
    for toss in range(TOSSES):
        result = random.randint(HEADS, TAILS)
        if result == HEADS:
            print == ("Heads") 
        else:
            print("Tails")
toss()