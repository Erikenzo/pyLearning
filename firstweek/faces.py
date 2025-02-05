def faces():
    face = str(input("Enter your face"))
    if face == ":)":
        return "🙂"
    if face == ":(":
        return "🙁"
    else:
        print("I do not recognise this face. Enter :) or :(")

def main():
    print(faces())

main()