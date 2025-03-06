def main():
    fraction = input("Fraction: ")
    print(convert(fraction))

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    fuel_level = int(x / y * 100)
    return gauge(fuel_level)


def gauge(percentage):
    try:
        if 0 <= percentage <= 100:
            if 0 <= percentage <= 1:
                return "E"
            elif 99 <= percentage <= 100:
                return "F"
            else:
                return f"{percentage}%"
    except (ValueError, ZeroDivisionError):
        pass


if __name__ == "__main__":
    main()