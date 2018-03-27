h = int(input("Enter lower range: "))
j = int(input("Enter upper range: "))
for i in range(h,j + 1):
   sum = 0
   temp = i
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
   if i == sum:
       print(i)
