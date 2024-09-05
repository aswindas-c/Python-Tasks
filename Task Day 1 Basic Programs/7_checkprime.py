num = int(input("Enter the number : "))
flag = 0
for i in range(2,int(num/2)):
    if num % i ==0:
        flag = 1
if flag ==0:
    print("The number is prime")
else:
    print("The number is not prime")