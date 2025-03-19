# Game of Hangman
import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class GameOfHangman:
    _list_of_words = ["Mystery", "Jungle", "Pyramid", "Thunder", "Knight", "Shadow", "Whisper", "Rocket", "Lantern", "Puzzle"]

    _hangman_stages = [
        """
           ------
           |    |
           |    
           |   
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |    
        --------
        GAME OVER!
        """
    ]
    def __init__(self):
        self._presented_word = random.choice(self._list_of_words).lower()
        self._guessed_word = ['_'] * len(self._presented_word)
        self._attempts = 6
        self._wrong_guesses = []

    

    def display_word(self):
        
        print(" ".join(self._guessed_word))
        print(GameOfHangman._hangman_stages[6 - self._attempts])
        print(f"Wrong guesses: {', '.join(self._wrong_guesses)}")
        print(f"Attempts left: {self._attempts}\n")


    def choosing_a_char(self):

        while self._attempts > 0 and '_' in self._guessed_word:
            clear_console()
            self.display_word()
            chosen_char = input('Choose a character> ')

            if not chosen_char.isalpha() or len(chosen_char) != 1:
                print('Incorrect input! Can not choose a number')
                continue
            
            if chosen_char in self._guessed_word or chosen_char in self._wrong_guesses:
                print(f"You already guessed '{chosen_char}'")
                continue

            
            if chosen_char in self._presented_word :
                for i, char in enumerate(self._presented_word):
                    if char == chosen_char:
                        self._guessed_word[i] = chosen_char
                print(f'Good guess! {chosen_char} is in the word.')
            elif chosen_char not in self._presented_word: 
                self._attempts -= 1
                self._wrong_guesses.append(chosen_char)
                print(f"Wrong guess! '{chosen_char}' is not in the word.")

        self.display_word()
        if "_" not in self._guessed_word:
            print(f"Congratulations! You guessed the word: {self._presented_word}")
        else:
            print(f"Game Over! The correct word was: {self._presented_word}")


game = GameOfHangman

if __name__ == "__main__":
    game.choosing_a_char()
   



