list =[]
n =  int(input("Enter the size of list : "))
print("Enter the elements of list : \n")
for i in range(0,n):
    num = int(input())
    list.append(num)
large = 0
second = 0
for i in range(0,n):
    if large<list[i]:
        second = large
        large=list[i]
print(f"Second Largest = {second}")
