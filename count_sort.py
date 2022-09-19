#count sort

arr1 = [3,2,7,9,8,5,1,0,2,11,2,3,1,1,0,0,6,5,4,3,2]

n = len(arr1)
arr2 =[]
arr2 = [0 for i in range(n)] 
for i in range(0,n):
    arr2[arr1[i]] =  arr2[arr1[i]] + 1

for i in range(0,n):
    j = i
    while (arr2[j] != 0) :
        print (i)
        arr2[j] = arr2[j] -1

