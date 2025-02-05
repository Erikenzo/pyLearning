def main():
    camel2Snake(quote)

def camel2Snake(quote):
    for letter in quote:
        if letter.isupper():
            print("_"+letter.lower(), end="")
        else:
            print(letter, end="")

quote = input("Camel case: ")

main()

