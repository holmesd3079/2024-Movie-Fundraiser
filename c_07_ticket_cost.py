import pandas


# Set currency into currency format
def currency(x):
    return f"${format(x, '.2f')}"


# Lists for pandas columns

all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

# Dictionary (for my panda frame)
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge,
}


mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index('Name')
# Calculate all totals and charges
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']
mini_movie_frame["Profit"] = mini_movie_frame['Ticket Price'] - 5

total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Ticket Price'] - 5

# Print calculated items
print(mini_movie_frame)
profit_string = f"Total Ticket sales: {currency(total)}\t Total Profit: {currency(profit.sum())}"
print(len(profit_string)*"-", "\n"+profit_string)
