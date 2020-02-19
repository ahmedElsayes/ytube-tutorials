
# algorithm for catcing the repeated consecutive elements in array

List = [2, 5, 8, 9, 10, 10, 28, 25]
length = len(List)
print(length)
for i in range(1, length, 1):
    for ii in range(i, length, 1):
        if List[ii] == List[i]:
            print("consecutive", i, List[i], ii, List[ii], List[0])
            break
        else:
            pass


#####################
# algorithm for catcing the repetead elements in array

List = [2, 5, 8, 9, 10, 10, 28, 25]
length = len(List)
print(length)
for i in range(2, length, 1):
    for ii in range(i-1, i, 1):
        if List[ii] == List[i]:
            print("repeated elements", i, List[i], ii, List[ii], List[0])
            break
        else:
            pass
