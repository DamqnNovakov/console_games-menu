
  # Tic-Tac-Toe Game 
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class GameBoard:
    _gamePlaying = True

    def __init__(self):
        self._board = [
            ['*', '*', '*'],
            ['*', '*', '*'],
            ['*', '*', '*']
        ]
        self._winner = None
        self._currentPlayer = 'X'

    def display_board(self):
        print('           Hello to Tic-Tac-Toe Game')
        print('-------------')
        print('| ' + self._board[0][0] + ' | ' + self._board[0][1] + ' | ' + self._board[0][2] + ' |')
        print('| ' + self._board[1][0] + ' | ' + self._board[1][1] + ' | ' + self._board[1][2] + ' |')
        print('| ' + self._board[2][0] + ' | ' + self._board[2][1] + ' | ' + self._board[2][2] + ' |')
        print('-------------')

        
    def playerMove(self):
        while True:
            move = int(input(f'{self._currentPlayer} a number from 1 to 9> ')) - 1
            row = move // 3
            col = move % 3
            if move >= 0 and move <= 9 and self._board[row][col] == '*':
                self._board[row][col] = self._currentPlayer
                break
            else:
                print('Incorrect move! Pick from 1 to 9!')
                continue

    def winningHorizontaly(self):
        if self._board[0][0] == self._board[0][1] == self._board[0][2] and self._board[0][0] != '*':
            self._winner = self._board[0][0]
            return True
        elif self._board[1][0] == self._board[1][1] == self._board[1][2] and self._board[1][0] != '*':
            self._winner = self._board[1][0]
            return True
        elif self._board[2][0] == self._board[2][1] == self._board[2][2] and self._board[2][0] != '*':
            self._winner = self._board[2][0]
            return True
        
    def winningVertically(self):
        if self._board[0][0] == self._board[1][0] == self._board[2][0] and self._board[0][0] != '*':
            self._winner = self._board[0][0]
            return True
        elif self._board[0][1] == self._board[1][1] == self._board[2][1] and self._board[0][1] != '*':
            self._winner = self._board[0][1]
            return True
        elif self._board[0][2] == self._board[1][2] == self._board[2][2] and self._board[0][2] != '*':
            self._winner = self._board[0][2]
            return True
    
    def winningDiagonally(self):
        if self._board[0][0] == self._board[1][1] == self._board[2][2] and self._board[0][0] != '*':
            self._winner = self._board[0][0]
            return True
        if self._board[0][2] == self._board[1][1] == self._board[2][0] and self._board[0][2] != '*':
            self._winner = self._board[0][2]
            return True

    def checkTie(self):   
        
        for i in self._board:
            for j in i:
                if j == '*':
                    return  
        self.display_board()
        print("It's a tie")
        self._gamePlaying = False


    def endGame(self):
        
        if self.winningHorizontaly() or self.winningVertically() or self.winningDiagonally() == True:
            clear_console()
            self.display_board()
            print(f'The winner is {self._winner}') 
            self._gamePlaying = False

    
    def switchPlayer(self):
        if self._currentPlayer == 'X':
            self._currentPlayer = 'O'
        else:
            self._currentPlayer = 'X'

    def gamePlay(self):
        print('''                                               Tick-Tack-Toe Game
        Rules:
        1.Players alternate turns to place their marks (X or O) in an empty cell of the 3x3 grid
        2.The first player to get 3 of their marks in a row wins the game.The row can be horizontal, vertical, or diagonal.
        3.If all spaces are filled and there is no winner, the game ends in a draw.
        ''')
        while self._gamePlaying == True:
            clear_console()
            self.display_board()
            self.playerMove()
            self.endGame()
            self.checkTie()
            self.switchPlayer()



game = GameBoard
if __name__ == "__main__":
    game.gamePlay()




