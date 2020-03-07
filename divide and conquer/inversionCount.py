from math import floor
def merge(arr, l, r):
    m = floor((l+r)/2)
    i = l
    j = m+1
    count = 0
    temp = list()
    while(i<=m and j<=r):
        if(arr[i]<=arr[j]):
            temp.append(arr[i])
            i+=1
        else:
            count+= m-i+1
            temp.append(arr[j])
            j+=1
    while(i<=m):
        temp.append(arr[i])
        i+=1
    while(j<=r):
        temp.append(arr[j])
        j+=1
    for i in range(len(temp)):
        arr[l+i] = temp[i]
    return count    
        
def inversionCount(arr, l, r):
    
    if l==r:
        return 0
    m = floor((l+r)/2)
    a = inversionCount(arr, l, m)
    b = inversionCount(arr, m+1, r)
    c = merge(arr, l, r)
    return a+b+c
    

arr = [10, 8, 6, 4, 2]   
print(arr)
print(inversionCount(arr, 0, 4))
print(arr)