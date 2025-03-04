def main():
    word = input()
    shorten(word)


def shorten(word):
    word = word.lower() # I have added .lower() here instead of line 2 to capture lowercase in tests easier.
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for letter in word:
        if not letter in vowels:
            print(letter, end="")
            result += letter

    return result


if __name__ == "__main__":
    main()