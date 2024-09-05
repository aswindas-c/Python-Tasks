def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
number = int(input("Enter the number : \n"))
print(f"Factorial = {factorial(number)}")