import random
#test change for github

class Game:
    player_count = 0
    players_list = []
    winning_score = 0
    def __init__(self):
        self.player_count = int(input("How many players?"))
        for num in range(self.player_count):
            #this calls the constructor for Player and adds each instance to the players_list
            self.players_list.append(Player(input("Please enter a name for Player{}:".format(num+1))))
        #this creates the score_dict with the player(key) and their score(value)
        self.score_dict = {player:player.player_score for player in self.players_list}
        self.winning_score = int(input("What score do you want to play to? (Standard is 50)"))
    
    def roll_dice(self, player):
        player.roll_again = True
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 == dice2:
            player.player_score = 0
            print("You rolled a double!!! {}'s score has reset to 0!!!".format(player))
            player.roll_again = False
            return
        else:
            score = dice1 + dice2
            player.player_score += score
            self.score_dict[player] += score
            print("Noice! You rolled a {}. {}'s score is now {}.".format(score, player, player.player_score))
            roll_request = input("Do you want to roll again (y / n)?")
            if roll_request == "n":
                player.roll_again = False
                return

   

class Player:
    player_number = 1
    def __init__(self, name= "Player{}".format(player_number)):
        self.name = name
        self.player_score = 0
        self.roll_again = False
    def __repr__(self):
        return self.name

    