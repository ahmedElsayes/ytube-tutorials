# ahmed.elsayes@tuni.fi
# Never mind this statement, for compatibility reasons
from __future__ import absolute_import, division, print_function, unicode_literals
# Make numpy available using np.
import numpy as np
def add_compare(x,y):
    if (30>x>10):
        print('30>x>10 and x = ', x)
    elif(x>30):
        print('x>30 and x = ', x)
    else:
        print('X<10 AND X = ', x)
    return x+y
# just to test the function of add_compare

print('this is new one')
z = add_compare(5,5)
print('z = ', z)

print('this is new one')
z = add_compare(15, 5)
print('z = ', z)

print('this is new one')
z = add_compare(35, 5)
print('z = ', z)

print('this is new one')
z = add_compare(20, 5)
print('z = ', z)

print('this is new one')
z = add_compare(2, 5)
print('z = ', z)

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

# test on using numby library
aa = np.array(['Ahmed', 'Elsayes', 'good start'])
aa = np.append(aa, '!')
# aa = aa.append(aa, 'good start')
iii = 1
for ii in aa:
    print('the array element', iii, ' =', ii)
    iii = iii + 1
#another format to print array elements and its index
for i, e in enumerate(aa):
    print('the element is {} and its index: {}'.format(e,i))

# somebasic operations from numpy library
b = np.array([2, 7, 9, 5, 12, 20, 15])
print('the maximum of array = {}'.format(np.max(b))) #the maximum of array
print('averag of the array ={}'.format(np.average(b))) # the average of the array
print('the index of the maximum number in the array ={}'.format(np.argmax(b))) # index ofmaximum number
# create an arrayof random numbers
C = np.random.rand(3,3)
print('C is a matrix = ', C)
# speculate the dimentions of the different arrays and the type of an element array and the array
print('the shape of aa is {}'.format(aa.shape))
print('the shape of b is {}'.format(b.shape))
print('the shape of C is {}'.format(C.shape))
print('the type of b is {} and type of b[0] is {}'.format(type(b), type(b[0])))     # type of variables
