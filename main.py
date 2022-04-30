import random
import time
import string
class ColourGame: 
    def __init__(self):
        self.square_names = [a+str(b) for b in range(1,9) for a in string.ascii_lowercase[:8]]
        self.correct_answers = 0
        self.tries = 0

    def __get_colour_of_square(self,coordinate):
        if (ord(coordinate[0]))%2 == int(coordinate[1]) % 2 :
            return "b"
        return "w"

    def ask_question(self):
        self.tries += 1 
        random_square =  random.choice(self.square_names)
        try:
            answer = input(f"What colour is {random_square}?")
            if answer == self.__get_colour_of_square(random_square):
                self.correct_answers += 1
                print("Correct!!!!!!")
                return True
            else:
                print("You Suck!")
        except(KeyboardInterrupt):
            print(""" 
                     
                    you stopped playing
                    """)
            exit()


if __name__ == "__main__":
    game_end = time.monotonic() + 60     
    game = ColourGame()
    while time.monotonic() < game_end:
        print(f"Time left {game_end-time.monotonic()}")
        game.ask_question()
    print(f"Your score was {game.correct_answers} / {game.tries} ")



