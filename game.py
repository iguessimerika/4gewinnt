import re

circle = "●";

def generate_board():
    """generates a 2d array, which is the template for an empty 4 wins board"""
    return [
            [" ", " ", " ", " ", " ", " ", " "], 
            [" ", " ", " ", " ", " ", " ", " "], 
            [" ", " ", " ", " ", " ", " ", " "], 
            [" ", " ", " ", " ", " ", " ", " "], 
            [" ", " ", " ", " ", " ", " ", " "], 
            [" ", " ", " ", " ", " ", " ", " "], 
        ]
    
def insert_circle(board, column, color):
    """insert the circle in the given column with the given color"""
    

def check_win(board):
    """checks for a win on the board"""