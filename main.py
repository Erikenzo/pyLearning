#adding comment to test git
#hell yeah conflict incoming

def start(age):
    return 2025-age

firstName, lastName =input("What is your name?").strip().title().split()

print(f"Nice to meet you {firstName}!")
print(f"I know someone with your last name {lastName}" )
age=int(input("How old are you?"))
print(f"He was also bon in {start(age)}")
