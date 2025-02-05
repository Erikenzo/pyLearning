def main():
    hh, mm = input("What time it is?").split(":")
    convertedTime = convert(int(hh), int(mm))
    if 7 <= convertedTime <= 8:
        print("Breakfast")
    elif 12< convertedTime <= 13:
        print("Lunch")
    elif 18 <= convertedTime <= 19:
        print("Dinner")
    else:
        print("No food rn, sorry")
    print(amOrPm(int(hh), int(mm)))

def convert(hh, mm):
    time = round(float(hh + mm / 60), 2)
    return time

def amOrPm(hh, mm):
    if hh >=13:
        time = f"{hh -12}:{mm} PM"

    return time

if __name__ == "__main__":
    main()