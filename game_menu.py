#  Hello to our Game Menu
import os
from game_of_hangman import GameOfHangman
from rock_paper_scissors import RockPapperCsissors
from Tic_Tac_Toe_game import GameBoard

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def game_menu():
    print('''
            Game Menu
          
    ---------------------------
    1.Hangman Game
    ---------------------------
    2.Rock-Papper-Scissors Game
    ---------------------------
    3.Tic-Tac-Toe Game
    ---------------------------
    Type 'Exit' to quit
    ''')

def start_game():
    while True:
        game_menu()
        choise = input("Choose the game you want to play (1-3)> ")
        if choise.isdigit():
            choise = int(choise) 
            if choise in [1, 2, 3]:
                play_game(choise) 
        elif choise.isalpha():
            choise.capitalize()
            if choise == 'Exit':
                quit()
        else:
                print("Incorrect value! Choose between (1-3)")
        

def play_game(choise):
    while True:
        clear_console()
        if choise == 1:
            game = GameOfHangman()
            game.choosing_a_char()
        elif choise == 2:
            game = RockPapperCsissors()
            game.game_logic()
        elif choise == 3:
            game = GameBoard()
            game.gamePlay()
        
        play_status = input('Do you want to continue playing? (Yes/No) or (Back) to return to the Game Menu> ').upper()
        if play_status == 'YES':
            continue
        elif play_status == 'NO':
            clear_console()
            break
        elif play_status == 'BACK':
            clear_console()
            start_game()

        
        
start_game()