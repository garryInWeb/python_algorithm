def insert_sort(lis):
    length = len(lis)
    for i in range(1,length-1):
        j = i - 1
        x = lis[i]
        while j > 0:
            if(x < lis[j]):
                lis[j+1] = lis[j]
                lis[j] = x
            j -= 1






lis = [8,5,2,3,0,5,8,7,854,6,8,64,65,46,54]
insert_sort(lis)
print(lis)
