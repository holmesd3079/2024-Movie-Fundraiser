def int_check(question, low_num=None, high_num=None, exit_code=None, can_float=False):
    situation = ""

    if low_num is not None and high_num is not None:
        situation = "both"
    elif low_num is not None and high_num is None:
        situation = "low only"
    while True:

        response = input(question)
        if response == exit_code:
            return response

        try:
            if can_float:
                response = float(response)
            else:
                response = int(response)

            if situation == "both":

                if response < low_num or response > high_num:
                    print(f"Please enter a number between {low_num} and {high_num}")

                    continue

            elif situation == "low only":
                if response <= low_num:
                    print(f"Please enter a number that is more than {low_num}")
                    continue

            return response

        except ValueError:
            if can_float:
                print("Please enter a Number")
            else:
                print("Please enter an integer")


while True:
    if int_check("Number", 0, exit_code="xxx") == "xxx":
        print("Exit")
        break
