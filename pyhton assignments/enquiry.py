
answer = (input("Answer Y or N: "))

while answer:

    if ((answer == "y") or (answer == "Y") or (answer == "n") or (answer == "N")):
        print("You answered", answer)
        break

    else:
        print("Incorrect entry.")
        answer = (input("Please retry: "))
