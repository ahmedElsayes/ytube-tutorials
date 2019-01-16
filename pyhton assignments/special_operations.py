
price = int(input("Purchase price: "))
paid = int(input("Paid amount of money: "))

subtraction = paid - price



# defining variables

var1 = subtraction // 10
var2 = subtraction % 10
var3 = var2 // 5
var4 = var2 % 5
var5 = var4 // 2
var6 = var4 % 2

# Logical operations

if price >= paid:
    print("No change")
else:
    print("Offer change: ")

if var1 > 0:
    print(var1," ten-euro notes")
else:
    pass

if var3 > 0:
    print(var3, " five-euro notes")
else:
    pass

if var5 > 0:
    print(var5, " two-euro coins")
else:
    pass

if var6 > 0:
    print(var6, " one-euro coins")
else:
    pass

