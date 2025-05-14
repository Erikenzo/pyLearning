import sys, csv

students = []
filtered_students = []


def checking_file():
        if len(sys.argv) == 3:
            if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
                # print(sys.argv[1])
                # print(sys.argv[2])
                # print(len(sys.argv))
                converting_names_and_houses(sys.argv[1])
                print(filtered_students)
                adding_to_after_file(sys.argv[2])
            else:
                sys.exit("This is not a CSV file")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")


def converting_names_and_houses(before_file):
    with open(before_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name" : row["name"], "house" : row["house"]})
    for student in sorted(students, key=lambda student:student["house"]):
        print("hi",end=" ")
        #print(f"{student['name']} is in {student['house']}")
        # writer = csv.DictWriter(after_file, fieldnames=["name", "house"])
        # writer.writerow({"name" : name, "house" : house})
    for student in sorted(students, key=lambda student: student["name"]):
        last_name, first_name = student['name'].split(", ")
        filtered_students.append({"first_name" : first_name, "last_name" : last_name, "house" : student["house"]})

def adding_to_after_file(after_file):
    with open(after_file, "a") as file: #for future me, I spent a hour figuring our why my code doesn't work, but I missed "a" LOL
        writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "house"])
        for student in filtered_students: #### understand how to write filtered_students in to CSV file and use syntax below without loop?
            writer.writerow({"first_name" :student["first_name"] , "last_name" : student["last_name"], "house" : student["house"]})

def main():
    checking_file()


main()
