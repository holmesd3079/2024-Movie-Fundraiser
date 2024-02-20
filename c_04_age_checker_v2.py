def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter a valid age")


while True:
    age = num_check("What is your age")
    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("You are too young for this Movie")
        continue
    else:
        print("There might of been a typo, please try again")
