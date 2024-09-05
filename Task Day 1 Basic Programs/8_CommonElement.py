list1 =[]
n =  int(input("Enter the size of list 1: "))
print("Enter the elements of list 1 : \n")
for i in range(0,n):
    num = int(input())
    list1.append(num)
list2 =[]
list3 = []
n =  int(input("Enter the size of list 2: "))
print("Enter the elements of list 2 : \n")
for i in range(0,n):
    num = int(input())
    list2.append(num)
print("Common Elements")
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)

