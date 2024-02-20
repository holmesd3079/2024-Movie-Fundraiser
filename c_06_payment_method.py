def cash_credit(question):
    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"
        elif response == "credit":
            return "credit"
        else:
            print("Please choose a valid method of payment")


while True:
    if cash_credit("Cash or credit") == "credit":
        print()
