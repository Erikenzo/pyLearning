def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    """
    Checks if a license plate is valid according to the following rules:
    - Minimum length of 2 characters, maximum length of 6 characters.
    - Must start with at least two letters.
    - All numbers, if any, must come at the end.
    - The first number used cannot be a '0'.
    """

    length = len(plate)

    if not (2 <= length <= 6):
        return False

    if not plate[:2].isalpha():
        return False

    letters = 0
    for char in plate:
        if char.isalpha():
            letters += 1
        else:
            break

    if letters == length:
        return True
    #returns true if all chars are letters in plate if not continues to check for numbers and spec symbols

    numbers = plate[letters:]

    if not numbers.isdigit():
        return False #returns false if remaining chars are != numbers, to eliminate spec symbols

    if numbers and numbers[0] == '0':
        return False

    return True

if __name__ == "__main__":
    main()