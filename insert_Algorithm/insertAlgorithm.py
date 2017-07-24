def insertAlgorithm( lis ):
    for i,x in enumerate(lis):
        for j,y in enumerate(lis[:i-len(lis)]):
            if(x < y):
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp







lis = [8,5,2,3,0,5,8,7,854,6,8,64,65,46,54]
insertAlgorithm(lis)
print(lis)