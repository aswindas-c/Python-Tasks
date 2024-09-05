try:
    num = int(input("Enter the number : "))
    if num < 1:
        print("Enter Positive Integer")
    else:
        flag = 0
        for i in range(2,int(num/2)):
            if num % i ==0:
                flag = 1
        if flag ==0:
            print("The number is prime")
        else:
            print("The number is not prime")
except ValueError:
    print("Enter Integer Value")