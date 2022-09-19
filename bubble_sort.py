#bubble sort

arr1 = [3,2,7,9,8,5,1,0,2,11]

n = len(arr1)

for j in range (0,n):
    for i in range(0,n-1 -j):
        if (arr1[i]>arr1[i+1]):
            arr1[i] , arr1[i+1] = arr1[i+1] , arr1[i]

for l in arr1:
    print (l)
