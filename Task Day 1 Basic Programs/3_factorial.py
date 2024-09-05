def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
try:
    number = int(input("Enter the number : \n"))
    print(f"Factorial = {factorial(number)}")
except ValueError:
    print("Enter a Integer Number")
except RecursionError:
    print("Enter Positive Number")
