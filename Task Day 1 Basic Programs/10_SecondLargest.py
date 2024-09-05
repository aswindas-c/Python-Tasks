import sys

number_list =[]
try:
    n =  int(input("Enter the size of list : "))
    print("Enter the elements of list : \n")
    for i in range(0,n):
        num = int(input())
        number_list.append(num)
    large =number_list[0]
    second = number_list[1]
    if large < second:
        temp = large
        large = second
        second = temp
    for i in range(2,n):
        if large<number_list[i]:
            second = large
            large=number_list[i]
        elif second<number_list[i]:
            second = number_list[i]
    print(f"Second Largest = {second}")
except ValueError:
    print("Enter Integer Number")
