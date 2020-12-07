from models.player import Player

class Game():

    
    def play_game_and_compare(player_1, player_2):
        if player_1.choice == "Rock" and player_2.choice == "Paper":
            return "The winner is {self.player2}"
        elif player_1.choice == "Rock" and player_2.choice == "Scissors":
            return "The winner is {self.player2}"
        elif player_1.choice == "Scissors" and player_2.choice == "Paper":
            return "The winner is {self.player2}"
        elif player_1.choice == player_2.choice:
            return None



