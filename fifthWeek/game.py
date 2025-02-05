import random

def game(prompt):
        try:
            level = int(input(prompt))
            if level > 0:
                play_game(level)
        except ValueError:
            pass


def play_game(level):
    number = random.randint(1, level)
    #print(f"{level} level and {number} number")
    while True:
        guess = int(input("Guess: "))
        if guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
        else:
            print("Just right!")
            return False



game("Level:")