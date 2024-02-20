def not_blank(question, err="This is blank, please enter real characters"):
    while True:
        response = input(question)
        if response:
            return response
        else:
            print(err)


while True:
    if not_blank('Is this blank ("xxx" to quit)').lower() == "xxx":
        break

print("We are done")
