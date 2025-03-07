import sys
from tabulate import tabulate


menu = []

def reading_menu():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1]) as file:
                for line in file:
                    menu.append(line.split(","))
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


def printing_table(menu):
    table = menu[1:]
    headers = menu[0]
    print(tabulate(table, headers, tablefmt="grid"))


def main():
    reading_menu()
    printing_table(menu)

main()

'''
Output with regular.csv
+-----------------+---------+---------+
| Regular Pizza   | Small   | Large   |
|                 |         |         |
+=================+=========+=========+
| Cheese          | $13.50  | $18.95  |
+-----------------+---------+---------+
| 1 topping       | $14.75  | $20.95  |
+-----------------+---------+---------+
| 2 toppings      | $15.95  | $22.95  |
+-----------------+---------+---------+
| 3 toppings      | $16.95  | $24.95  |
+-----------------+---------+---------+
| Special         | $18.50  | $26.95  |
+-----------------+---------+---------+
Output with sicilian.csv
+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
|                  |         |         |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+
'''