yes_no = ["yes", "no"]


# Choice checker/Default to yes_no checker if only Question is inputted
def choice_checker(question, chosen_valids=None, error=None):
    valid = False
    # If no chosen valid, default to yes/no checker
    if chosen_valids is None:
        chosen_valids = yes_no
        error = "Pick yes or no"

    # Repeat question if it does nothing match's the list
    while not valid:
        response = input(question).lower()
        # Loop through list of valids with the input
        for item in chosen_valids:
            if response == item[0] or response == item:
                # Return matched valid
                return item

        print(error)


while True:
    if choice_checker("Do you want instructions") == "yes":
        print("{Instructions}")

    print("Continues...")
