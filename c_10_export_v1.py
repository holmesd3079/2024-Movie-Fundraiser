import pandas
import random
from datetime import date

today = date.today()
sh_date = f"{today.day}_{today.month}_{today.year}"
filename = f"MF_{sh_date}"

print(filename)


def currency(x):
    return f"${format(x, '.2f')}"


# Lists for pandas columns

all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge,
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price'] - 5

winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

mini_movie_frame = mini_movie_frame.set_index('Name')

mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Ticket Price'] - 5

print(mini_movie_frame)
print()
winner_string = f"\n---- Raffle Winner ----\n" \
                f"Congratulation {winner_name}. You have won {currency(total_won)}"
print(winner_string)

print("\n\n\n")
to_write = f" ---- Mini Movie Fundraiser Ticket Data {filename} ----\nTicket cost / Profit\n{mini_movie_string}" \
           f"\n\nTotal: {currency(total)} | Profit: {currency(profit.sum())} \n{winner_string}"

print(to_write)

text_file = open(f"{filename}.txt", "w+")

text_file.write(to_write)
text_file.close()
