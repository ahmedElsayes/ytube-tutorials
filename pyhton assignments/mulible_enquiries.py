
answer = (input("Bored? (y/n) "))

while answer:

    if ((answer == "y") or (answer == "Y") ):
        print("Well, let's stop this, then.")
        break

    elif ((answer == "n") or (answer == "N")):
        answer = (input("Bored? (y/n) "))

    else:
        print("Incorrect entry.")
        answer = (input("Please retry: "))




