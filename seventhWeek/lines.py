import sys

def reading_comand():
    #checking how many arguments are passed, if 2 looking if 2nd item is python file
    if len(sys.argv)==2:
        if sys.argv[1].endswith(".py"):
            try:
                reading_file_v1(sys.argv[1])
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            print("Not a Python file")
            exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        exit()
    else:
        print("Too few command-line arguments")
        exit()

def reading_file_v1(filename):
    with open(filename) as file:
        code_lines_count = 0
        for line in file:
            if not line.strip().startswith("#") and line.strip():
                print(line, end="")
                code_lines_count += 1
    print(code_lines_count)

def exit():
    sys.exit()

def main():
    reading_comand()
main()
