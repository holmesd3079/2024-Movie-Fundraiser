import pandas
import random

# Set Max tickets to 50 and tickets sold to zero
max_tickets = 50
sold_tickets = 0

all_names, all_ticket_costs, all_ages, all_surcharge, all_payments = [], [], [], [], []


# Turn floats into currency format
def currency(x):
    return f"${format(x, '.2f')}"


# Detects if string is blank
def not_blank(question, err="This is blank, please enter real characters"):
    while True:
        response = input(question)
        if response:
            return response
        else:
            print(err)


# Asks given question and checks if it is a number
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter a valid age")


# Turning number(age) into prices
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


# Asks user if they want instructions
if choice_checker("Do you want to see the instructions") == "yes":
    print("{instructions}")
print()

# Main loop
while sold_tickets < max_tickets:
    # Asks for users name (checks if it is not blank
    name = not_blank("What is your first Name? ")
    if name == "xxx":
        break
    # Asks users age and checks if it is a number
    age = num_check("What is your age ")
    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("You are too young for this Movie")
        continue
    else:
        # If they are oddly too old
        print("There might of been a typo, please try again")
        continue

    ticket_cost = ticket_price(age)

    # Cash or credit
    payment_method = choice_checker("Cash or credit: ", ("cash", "credit"), "Please pick cash or credit", 2)
    if payment_method == "cash":
        surcharge = 0
    else:
        surcharge = 0.05 * ticket_cost
    # Set all items up for PANDAS and to set values
    sold_tickets += 1
    all_names.append(name)
    all_ages.append(age)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)
    all_payments.append(payment_method)
    print(f"Age: {age}, Ticket price: {currency(ticket_price(age))}, you paid {payment_method}\n")

if sold_tickets == max_tickets:
    print(f"You have sold {sold_tickets} of the tickets!")
else:
    print(f"{sold_tickets} Tickets have been sold. | You have {max_tickets - sold_tickets} Tickets left to sell.")

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge,
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate all totals and charges
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']
mini_movie_frame["Profit"] = mini_movie_frame['Ticket Price'] - 5


total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Ticket Price'] - 5

winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

mini_movie_frame = mini_movie_frame.set_index('Name')

# Print calculated items
print(mini_movie_frame)


profit_string = f"Total Ticket sales: {currency(total)}\t Total Profit: {currency(profit.sum())}"
print(len(profit_string)*"-", "\n"+profit_string)
print("\n---- Raffle Winner ----")
print(f"Congratulation {winner_name}. You have won {currency(total_won)}")