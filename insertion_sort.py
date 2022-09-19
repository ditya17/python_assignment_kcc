#insertion sort

arr1 = [3,2,7,9,8,5,1,0,2,11]

for i in range(0,10):
    for j in range(i,0,-1):
        if (arr1[j] < arr1[j-1]) :
            arr1[j] , arr1[j-1] = arr1[j-1], arr1[j]

for l in arr1:
    print (l)
    
    
    
