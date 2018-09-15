def runnerup(n, a):
    # finding the highest scorer
    max = a[0]
    for i in range(n):
        if max < a[i]:
            max = a[i]
    
    # creating an array without max
    arr = []
    for i in range(n):
        if max != a[i]:
            arr.append(a[i])
            
    
    # finding out the rummer up score
    rup = arr[0]
    for i in range(len(arr)):
        if rup < arr[i]:
            rup = arr[i]
    
    print("Rummer up = ", rup)

runnerup(5,[4, 7, 8, 3, 2])