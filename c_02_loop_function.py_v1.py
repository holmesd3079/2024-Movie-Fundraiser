max_tickets = 3
sold_tickets = 0
while sold_tickets < max_tickets:
    name = input("What is your first Name?")
    if name == "xxx":
        break
    sold_tickets += 1


if sold_tickets == max_tickets:
    print(f"You have sold {sold_tickets} of the tickets!")
else:
    print(f"{sold_tickets} Tickets have been sold. | You have {max_tickets - sold_tickets} Tickets left to sell.")
