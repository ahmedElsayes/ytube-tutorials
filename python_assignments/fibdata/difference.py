# import numpy as np
def subtractor(list):
    length = len(list)
    result=[]
    for i in range(1,length,1):
        ii = list[i]-list[i-1]
        result.append(ii)
    return result


# Z = np.linspace(2, 10, num=5)
# A = [2, 5, 7, 9, 12, 14, 16]
# B = [2, 5, 7, 9, 2, 2, 2]
# C = np.divide(A,B)
# values = Z[np.array([1,4])]
# print(values)
# rr = subtractor(A)
# print(rr)
