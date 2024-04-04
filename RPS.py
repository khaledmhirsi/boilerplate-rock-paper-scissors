# The example function below keeps track of the opponent's history and plays 
# whatever the opponent played two plays ago. 
# It is not a very good player so you will need to change the code to 
# pass the challenge.

import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)



    guess = ["R", "P", "S"][random.randint(0, 2)]
    return guess
