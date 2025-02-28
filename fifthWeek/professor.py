#task https://cs50.harvard.edu/python/2022/psets/4/professor/

import random

def main():
    level = get_level()
    solved, not_solved = generate_integer(level)
    print(f"You have solved {solved} questions correctly and failed {not_solved}")


def get_level():
    while True:
        level = input("Level: ")
        while 0 < int(level) < 4:
            return int(level)



def generate_integer(level):
    problems = 10
    solved = 0
    not_solved = 0
    for i in range(problems):
        x = random.randint(0, 10*level)
        y = random.randint(0, 10*level)
        user_input = input(f"{x} + {y} = ")
        if int(user_input) != x+y:
            print("EEE")
            solved +=1
        else:
            not_solved +=1
    return solved, not_solved



if __name__ == "__main__":
    main()