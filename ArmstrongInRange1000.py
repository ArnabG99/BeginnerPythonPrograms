for num in range(2,1000):
    copy = num
    sum = 0
    while(copy>0):
        digit = copy % 10
        copy = int(copy / 10)
        sum = sum + digit**3
    if(sum == num):
        print(num)
        

        