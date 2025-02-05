def calculation(kilos):
    return kilos*pow(300000000,2)

def main():
    kilos= int(input("Please enter how many kilos: "))
    print(f"We converted {kilos} in to {calculation(kilos)} Joulies")

main()