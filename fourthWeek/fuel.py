def main():
    x = display_fuel("Fraction: ")
    print(x)

def display_fuel(prompt):
    while True:
        x, y =input(prompt).split("/")
        x = int(x)
        y= int(y)
        fuel_level = int(x/y*100)
        try:
            if 0 <= fuel_level <= 100:
                if 0 <= fuel_level < 2:
                    return "E"
                elif 98 < fuel_level <= 100:
                    return "F"
                else:
                    return f"{fuel_level} %"
        except (ValueError, ZeroDivisionError):
            pass

main()