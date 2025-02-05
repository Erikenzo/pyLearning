nutri_table = {
    "Apple" : 130,
    "Avocado" : 50,
    "Sweet Cherries" : 100
}

request = input("Item: ")

for item in nutri_table:
    if item == request:
        print(nutri_table[request])
