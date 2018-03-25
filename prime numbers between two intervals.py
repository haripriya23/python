h = int(input("Enter lower range:"))
j = int(input("Enter upper range:"))
for num in range(h,j+1):
    if num>1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            print(num)
