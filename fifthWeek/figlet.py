import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet() #set figlet to be Figlet() to not type Filget() each time, but type figlet
def words_to_print():
    if len(sys.argv) == 1:
        figlet.setFont(font=choice(figlet.getFonts()))
        print("Output:", figlet.renderText(input("Input: ")), sep="\n")

    # I am checking if I typed instructions nad if those instructions contain font from fonts here
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") in figlet.getFonts():
        figlet.setFont(font=choice(figlet.getFonts()))
        print("Output:", Figlet(font=sys.argv[2]).renderText(input("Input: ")), sep="\n")

    else:
        sys.exit("Invalid usage")



words_to_print()




