def main():
    greeting = input("Geeting: ")
    print(value(greeting))


def value(greeting):
    value = 0
    if "hello" in greeting.lower():
        value = 0
    elif greeting.lower().startswith("h"):
        value = 20
    else:
        value = 100
    return value

if __name__ == "__main__":
    main()


