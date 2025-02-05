months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def date_converter(prompt):
    while True:
        try:
            full_date = input(prompt)
            month, day, date = full_date.split("/")
            if int(day) <= 31 and int(month) <= 12:
                print(f"{date}-{month}-{day}")
                if month in months:
                    print(f"{date}-{months[month + 1]}-{day}")
        except ValueError:
            month, day, date = full_date.split(" ") #I can access full_date due to try does pass info further.
            day = day.strip(",") # removing ',' after day
            month = month.title() # keeping Month always start with capital letter
            if int(day) <= 31 and month in months:
                print(f"{date}-{months.index(month)+1}-{day}")
        except EOFError:
            return


date_converter("Date: ")