def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if ((len(plate) == 6 and plate[3:].isnumeric() and plate[3] != "0") and plate[0:3].isalpha()) or\
            ((len(plate) == 4 and plate[2:].isnumeric() and plate[2] != "0") and plate[0:2].isalpha()):
        if plate.isspace():
            return False
        else:
            return True


main()