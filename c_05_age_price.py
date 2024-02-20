# age_prices = {{16, 7.5}, {65, 10.5}} (temp)

def ticket_price(val_age):
    if val_age < 16:
        price = 7.5
    elif val_age < 65:
        price = 10.5
    else:
        price = 6.5

    return price


while True:
    age = int(input("Age: "))
    print(f"Age: {age}, Ticket price: ${format(ticket_price(age), '.2f')}")
    print()
