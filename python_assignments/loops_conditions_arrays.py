## operations on strings
import time
import consecutive_test as test
# from consecutive_test import catch_repeated
var1 = "Ahmed"
var2 = "mohamed"

print(var1[3], var2[0])  ## print the letter form the word according its position
print(var1[:3], var2[:2])
print(var1[-1], var2[:])


## if codition
name = "ihsan"
if name is "Ahmed":
    print("Hello ahmed")
elif name is "umar":
    print("Hello umar")
elif name is "ihsan":
    print("Hello ihsan")
elif name is "katr":
    print("Hello katr")
else:
    print("not defined")


## example on for loop in range
for t in range(5, 80, 5):   # (start, stop, step)
    print(t+2)

## example on while loop
u = 2
while u < 15:
    print(u)
    u += 3
    if (u >= 10):
        break

## Example on for loop to make a program counts all numbers except some in list
print("Example to make a program counts all numbers except some in list")
numlist = [5, 7, 96, 87, 25, 12, 30, 1, 8, 40, 45, 50]
for xx in range(0, 80, 5):  # (start, stop, step)
    if xx in numlist:
        continue
    print(xx)
## Example on for loop to make a program counts all numbers in specific range that included in the list only 
print('example to count only ten multiplied numbers')
number_list2 = [7, 5, 25, 40, 80, 90, 58, 63, 30, 587, 10]
for xx2 in range(0,110,10):
    if xx2 in number_list2:
        print(xx2)
    else:
        continue

## Example on defining functions
print("this example to show the use of functions")


def Ahmed(mm, nn):
    annual_salary = (12*mm)
    print("your annual salary is:", annual_salary)
    print("your age is:", nn)


Ahmed(300, 27)


def gendertype(gender="unknown"):
    if gender is "m":
        gender = "male"
    elif gender is "f":
        gender = "female"
    print(gender)
    pass

gendertype("m")
gendertype("f")
gendertype()

## example on unlimited number of arguments


def add_numbers(*args):     # the function add all elements in the array whatever the length
    total = 0
    for a in args:
        total += a
    print(total)


add_numbers(5, 10, 15, 20, 5, 4, 1)

## operations on the array length, minimum and maximum...........................................
## example for pushing numbers in array..........
list = []
for A in range(0, 30, 5):
    list.append(A)
    print(list)

b1 = len(list)
c1 = max(list)
d1 = min(list)
print(b1, c1, d1)

## for loop
for f in list[:5]:   # print elements of array from 1 to 5
    print(f)

for g in list[4:]:     # print last 4 elements of array
    print(g)
for z in list[-1:]:
    time.sleep(1)       # example of introducing delay in the python script
    print(z)

# example on calling a fuction from another script in this script 

List = [2, 5, 8, 9, 10, 10, 28, 25, 9, 22, 8, 36, 88, 88]
test.catch_consecutive(List)
test.catch_repeated(List)
# catch_repeated(List)
z = test.add_compare(20,5)
print('z = ', z)

# creat a list with specific range
list5 = [*range(5,90,5)]
print('list5...............', list5[-5:-1])