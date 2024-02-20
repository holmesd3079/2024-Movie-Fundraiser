import pandas

max_tickets, sold_tickets = 3, 0


def currency(x):
    return f"${format(x, '.2f')}"


def not_blank(question, err="This is blank, please enter real characters"):
    while True:
        response = input(question)
        if response:
            return response
        else:
            print(err)


def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter a valid age")


def ticket_price(val_age):
    if val_age < 16:
        price = 7.5
    elif val_age < 65:
        price = 10.5
    else:
        price = 6.5

    return price


# Choice checker - If a question but nothing else is put in it defaults to a yes_no checkers
def choice_checker(question, chosen_valid=("yes", "no"), error="Pick yes or no", skip_char=1):
    while True:
        response = input(question).lower()

        # Loop through list of valid with the input
        for item in chosen_valid:
            if response == item[:skip_char] or response == item:
                # Return matched valid
                return item

        print(error)


if choice_checker("Do you want to see the instructions") == "yes":
    print("{instructions}")
print()

while sold_tickets < max_tickets:
    name = not_blank("What is your first Name? ")
    if name == "xxx":
        break

    age = num_check("What is your age ")
    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("You are too young for this Movie")
        continue
    else:
        print("There might of been a typo, please try again")
        continue
    payment_method = choice_checker("Cash or credit: ", ("cash", "credit"), "Please pick cash or credit", 2)

    sold_tickets += 1

    print(f"Age: {age}, Ticket price: ${format(ticket_price(age), '.2f')}, you paid {payment_method}\n")
if sold_tickets == max_tickets:
    print(f"You have sold {sold_tickets} of the tickets!")
else:
    print(f"{sold_tickets} Tickets have been sold. | You have {max_tickets - sold_tickets} Tickets left to sell.")
