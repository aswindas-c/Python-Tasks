number_list =[]
try:
    n =  int(input("Enter the size of list : "))
    print("Enter the elements of list : \n")
    for i in range(0,n):
        num = int(input())
        number_list.append(num)
    large = list[0]
    for i in range(0,n):
        if large<number_list[i]:
            large=number_list[i]
    print(f"Largest = {large}")
except ValueError:
    print("Enter Integer Value")
