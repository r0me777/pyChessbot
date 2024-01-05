# Description: This file contains the implementation of the minimax algorithm


class Minimax: 
    def __init__(self):
        pass


    def heuristic(self, board_state): # Material Balance heurstic
        piece_values = {"p": 1, 
                        "n": 3, 
                        "b": 3, 
                        "r": 5, 
                        "q": 9, 
                        "k": 100}

        white_score = 0
        black_score = 0
        for row in board_state:
            for cell in row:
                if cell.isupper():
                    white_score += piece_values[cell.lower()]
                
                elif cell.islower():
                    black_score += piece_values[cell]
        
        return white_score - black_score


    def minimax(self, is_maximizing, depth):
        pass




        




        