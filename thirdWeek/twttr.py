def tweet():
    vowels = ["a", "e", "i", "o", "u"]
    user_input = input("Input: ")
    for letter in user_input:
            if not letter in vowels:
                print(letter, end="")
tweet()
