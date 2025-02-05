foodMenu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    order("Item: ")

def order(prompt):
    totalBill = 0
    while True:
        try:
            item = input(prompt).title()
            if item in foodMenu:
                totalBill += foodMenu[item]
                print(f"${totalBill:.2f}")
        except (ValueError):
            pass
        except EOFError:
            print("Thank you for your order!")
            break
main()
