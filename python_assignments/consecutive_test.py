
# algorithm for catcing the repeated consecutive elements in array
def catch_repeated(list):
    filt=[]
    # print(length2)
    for i in list:
        if i in filt:
            print('repeated element is {} with index of {}'.format(i, list.index(i)))
        else:
            filt.append(i)
            continue
#####################
# algorithm for catching the repetead elements in array
def catch_consecutive(list2):
    # List = [2, 5, 8, 9, 10, 10, 28, 25]
    length2 = len(list2)
    # print(length2)
    for i in range(1, length2, 1):
        for ii in range(i-1, i, 1):
            if list2[ii] == list2[i]:
                print("repeated consecutive elements", ii, list2[i], i, list2[ii])
                break
            else:
                pass

def add_compare(x,y):
    if (30>x>10):
        print('30>x>10 and x = ', x)
    elif(x>30):
        print('x>30 and x = ', x)
    else:
        print('X<10 AND X = ', x)
    return x+y