def song(prompt):
    while True:
        try:
            names.append(input(prompt))
        except EOFError:
            return print(names)

def printing(names):
    if len(names) != 0:
        for name in names:
            if name == names[0]:
                print(f"Adieu, adieu, to {names[0]}", end=" ")
            elif len(name) > 1 and name == names[-1]:
                print(f", and {name}", end=" ")
            else:
                print(f", {name}", end=" ")


names = []
song(("Name: "))
printing(names)