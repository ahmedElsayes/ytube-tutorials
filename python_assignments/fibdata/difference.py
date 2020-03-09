def subtractor(list):
    length = len(list)
    result=[]
    for i in range(1,length,1):
        ii = list[i]-list[i-1]
        result.append(ii)
    return result
