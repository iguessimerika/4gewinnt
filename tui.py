import os
import rich
from rich.prompt import Prompt

def starting_screen():
    """clears the terminal and shows the game name at the top of the terminal"""
    clear_screen()
    print(f"{"="*8} 4 GEWINNT {"="*8}\n")

    
def clear_screen():
    """clears the terminal"""
    os.system("cls" if os.name == "nt" else "clear")
    
def spacer():
    """prints a spacer for in between the board and the player entry"""
    print(f"\n\n{"="*25}\n\n")


def player_entry():
    """asks the user for 2 player names and saves them in a dictionary with their color"""
    
    player1 = input("Name Spieler 1: ")
    player2 = input("Name Spieler 2: ")
    
    player_data = {
        "player1": {
            "name": player1,
            "color": "blue"
        },
        "player2": {
            "name": player2,
            "color": "red"
        }
    }
    
    return player_data

def display_board(board):
    """displays the given 2d list as the board in the terminal"""
    starting_screen()
    spacer()
    
    border = "+---+---+---+---+---+---+---+"
    
    # top row - numbers for columns
    print(border)
    
    curr_row = 1
    for row in board:
        rich.print(f"  {curr_row}  | {row[0]} | {row[1]} | {row[2]} |")
        print(border)
        
        curr_row += 1
        
def display_result():
    """displays the winner or a tie"""