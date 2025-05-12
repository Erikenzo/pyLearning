import sys

def checking_file():

        if len(sys.argv) == 3:
            if sys.argv[1].endswith(".csv"):
                converting_names_and_houses(sys.argv[1], sys.argv[2])
            else:
                sys.exit("This is not a CSV file")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")


def converting_names_and_houses(before_file, after_file):
    with open(before_file) as file:
        for line in file:
            name, house = line.

def main():
    checking_file()

main()