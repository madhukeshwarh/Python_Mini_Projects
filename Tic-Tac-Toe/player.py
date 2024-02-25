import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def get_move(self, game):
        valid_square = False

        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (0-8): ")

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError("Invalid square. Please enter a number between 0 and 8.")
                
                valid_square = True
            
            except ValueError as e:
                print(e)

        return val
