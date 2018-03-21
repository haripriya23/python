a=int(input("Enter number: "))
j=0
for i in range(2,a//2+1):
    if(a%i==0):
        j=j+1
if(j<=0):
    print("Number is prime")
else:
    print("Number isn't prime")
