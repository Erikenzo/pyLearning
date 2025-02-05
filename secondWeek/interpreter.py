x, y, z = input("Equation: ").split(" ")

def calculation(x, y, z):
    if y == "+":
        return int(x) + int(z)
    elif y == "-":
        return int(x) - int(z)
    elif y == "*":
        return int(x) * int(z)
    elif y == "/":
        return int(x) / int(z)

print(round(float(calculation(x, y, z)), 2))

