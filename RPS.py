

def player(prev_play, opponent_history=[], counter=[0]):
    if prev_play != "":
        opponent_history.append(prev_play)
    
    if counter[0] <= 1000: # VS abbey
        counter[0] += 1     
        winning_pattern = ["P", "R", "S", "S", "R"]   
        return winning_pattern[counter[0] % len(winning_pattern)]
    elif counter[0] <= 3000: # VS kris and mrugesh
        counter[0] += 1
        return ["P", "R", "S"][counter[0] % 3]
    else: # VS quincy
        counter[0] += 1
        return ["P", "P", "S", "S", "R"][counter[0] % 5]