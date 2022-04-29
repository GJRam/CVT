import random
import time

class ColourGame: 
    def __init__(self):
        self.square_names = [
            "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8",
            "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
            "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
            "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8",
            "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8",
            "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
            "g1", "g2", "g3", "g4", "f5", "g6", "g7", "g8",
            "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8",
        ]
        self.correct_answers = 0
        self.tries = 0


    def __get_colour_of_square(self,coordinate):
        if (ord(coordinate[0]))%2 == int(coordinate[1]) % 2 :
            return "b"
        return "w"

    def ask_question(self):
        self.tries += 1 
        random_square =  random.choice(self.square_names)
        answer = input(f"What colour is {random_square}?")
        if answer == self.__get_colour_of_square(random_square):
            self.correct_answers += 1
            print("Correct!!!!!!")
            return True
        else:
            print("You Suck!")

        




if __name__ == "__main__":
    game_end = time.monotonic() + 60     
    game = ColourGame()
    while time.monotonic() < game_end:
        print(f"Time left {time.monotonic() - game_end}")
        game.ask_question()
    print(f"Your score was {game.correct_answers} / {game.tries} ")



