list =[]
n =  int(input("Enter the size of list : "))
print("Enter the elements of list : \n")
for i in range(0,n):
    num = int(input())
    list.append(num)
large = list[0]
for i in range(0,n):
    if large<list[i]:
        large=list[i]
print(f"Largest = {large}")
