def calc():
    due = 50
    while True:
        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            due -= coin

        if due == 0:
            print(f"Change Owned: {due}")
            break
        elif due <= 0:
            print(f"Change Owned: {due * -1}")
            break

calc()
