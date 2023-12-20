# roll a dice game for multiplayers,If if 1 appers while random dice roll.
# another player will start rolling. if sum of output after roll is 40 or more, the player wins



import random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value , max_value)
    return roll

while True:
     players = input ("\n ENTER the no. of players : \n ")
     if players.isdigit():
         players=int(players)
         if 1<=players<=4:
             break
         else:
             print("Must be between 2-4")
     else:
         print("invalid !! TRY AGAIN !!!")
max_score = 30

# storing each players score in a list with range of numbers of players
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print ("\nplayer", player_idx+1, " 's turn has begin \n")
        print("Your total score is:", player_scores[player_idx],"\n")
        Current_score = 0
        while True:
            keep_rolling = input("would u like to roll ?. Press (Y) to confirm ")
            if keep_rolling.lower() != "y":
                break

            value = roll()
            if value == 1:
                print(" you rolled 1, Your turn is out ")
                Current_score = 0
                break
            else:
                Current_score += value
                print("you rolled a: ", value)
            print("your score is: ", Current_score)
        player_scores[player_idx] += Current_score
        print("your total score is: ", player_scores[player_idx])

max_score = max(player_scores)
winning_player = player_scores.index(max_score)
print("player ,", winning_player + 1,"is the winner with the score of:", max_score)


