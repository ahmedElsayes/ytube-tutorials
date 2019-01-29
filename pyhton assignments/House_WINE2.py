# TIE-02106 Introduction to Programming
# Ahmed Elsayes, ahmed.elsayes@tuni.fi, student nr: 272537
# Solution of task 3.4:
# A program that determines on the validity of fermintation process of the wine.
# X represent the number of measurements and Y temperature values

X = int(input("Enter the number of measurements: "))
Z = (X*0.1)
list = []       # array for measurements out of range
list3 = [0]      # array for repeatitive measurements out of the range

def main(XX):

    if XX > 0:

        Y = int(input("Enter the temperature ii: "))
        TEMPERATURE_CONTROL(Y)

    else:
        print("The number of measurements must be a positive number.")


def TEMPERATURE_CONTROL(YY):

    for i in range(1, X, 1):
        YY = int(input("Enter the temperature i: "))
        if (20 >= YY) or (YY >= 25):
            list.append(YY)
        else:
            pass
        list3.append(YY)
        global array_length
        array_length = len(list)

        if (array_length > Z) or (list3[i] == list3[i-1]):
            print("Your wine is ruined.")
            break
        else:
            pass

        print(YY, array_length)

main(X)
