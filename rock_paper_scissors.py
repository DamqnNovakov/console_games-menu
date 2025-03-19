import random


class RockPapperCsissors:
    def __init__(self):
        self._result = ''
        self._player_score = 0
        self._computer_score = 0

    def computer_generated_move(self):
        random_float = random.random()
        computer_pick = ''
        if random_float >= 0 and random_float <= 1/3:
            computer_pick = 'Rock'
        elif random_float > 1/3 and random_float < 2/3:
            computer_pick = 'Papper'
        elif random_float >= 2/3 and random_float <= 1:
            computer_pick = 'Scissors'
        return computer_pick
    
    def game_logic(self):
        computer_pick = self.computer_generated_move()
        self.result = ''
        print('      Hello to out game of Rock-Papper-Scissors')
        game_entry = input('Do you want to play a game? (Yes/No) ').lower()
        
        while game_entry == 'yes':
            player_pick = input('Pick one of the options: (Rock/Papper/Scissors) or Q to quit the game.> ').capitalize()

            if player_pick not in ['Rock', 'Papper', 'Scissors', 'Q']:
                print('Invalid pick')
                continue

            if player_pick == 'Rock' and computer_pick == 'Papper':
                self.result = 'You lose'
                self._computer_score += 1
            elif player_pick == 'Scissors' and computer_pick == 'Rock':
                self.result = 'You lose'
                self._computer_score += 1
            elif player_pick == 'Papper' and computer_pick == 'Rock':
                self.result = 'You win'
                self._player_score += 1
            elif player_pick == 'Scissors' and computer_pick == 'Papper':
                self.result = 'You win'
                self._player_score += 1
            elif player_pick == 'Papper' and computer_pick == 'Scissors':
                self.result = 'You lose'
                self._computer_score += 1
            elif player_pick == 'Rock' and computer_pick == 'Scissors':
                self.result = 'You win'
                self._player_score += 1
            elif player_pick == computer_pick:
                print(f'Player picked {player_pick} and Computer picked {computer_pick}')
                print('Tie')
                print(f'You {self._player_score} : Computer {self._computer_score}')
                continue
            elif player_pick == "Q":
                print('Thank you for playing!')
                print('Final result')
                print(f'You {self._player_score} : Computer {self._computer_score}')
                break
           
            print(f'You picked: {player_pick} : Computer picked: {computer_pick}')
            print(f'Result : {self.result}')
            print(f'You {self._player_score} : Computer {self._computer_score}')
            continue

   
game = RockPapperCsissors
if __name__ == "__main__":
    game.game_logic()


        


