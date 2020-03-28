import _thread
import time

list1 = [*range(5, 300, 1)]
list2 = [*range(5, 400, 2)]
C = []


def loop1(A, delay1):
    for i, e in enumerate(A):
        time.sleep(delay1)
        C.append(e)
        print('loop1: element{}: {}'.format(i, e))


def loop2(B, delay2):
    for i, e in enumerate(B):
        time.sleep(delay2)
        print('loop2: element{}: {}'.format(i, e))


_thread.start_new(loop1, (list1, 0.3))
_thread.start_new(loop2, (list2, 0.2))

while 1:
    if len(C) == len(list1):
        break
    else:
        pass
# ...........................
x = 15
def change():
    # using a global keyword
    global x
    # increment value of a by 5
    x = x + 5
    print("Value of x inside a function :", x)
change()
print("Value of x outside a function :", x)
