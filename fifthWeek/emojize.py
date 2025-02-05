import emoji

def emoji_translator():
    while True:
        try:
            emoji_input = input("Input: ")
            print(emoji.emojize(f"Output: {emoji_input}"))
        except EOFError:
            break


emoji_translator()