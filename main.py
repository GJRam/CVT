import random

square_names = [
        "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8",
        "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
        "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
        "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8",
        "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8",
        "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
        "g1", "g2", "g3", "g4", "f5", "g6", "g7", "g8",
        "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8",
    ]


def __get_colour_of_square(coordinate):
    if (ord(coordinate[0]))%2 == int(coordinate[1]) % 2 :
        return "b"
    return "w"


def __ask_question():
    random_square =  random.choice(square_names)
    answer = input(f"What colour is {random_square}?")
    if answer == __get_colour_of_square(random_square):
        print("Correct!!!!!!")
        return True
    else:
        print("you suck!")
        return False

    print(f"Your score is {counter} out of {tries}")

        




if __name__ == "__main__":
    counter = tries = 0
    while(True):
        tries += 1
        if __ask_question() == True:
            counter += 1
            print(f"Score is {counter} over {tries}")
        else:
            print(f"Score is {counter} over {tries}")



