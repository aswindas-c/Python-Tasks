list1 =[]
n =  int(input("Enter the size of list 1: "))
print("Enter the elements of list 1 : \n")
for i in range(0,n):
    num = int(input())
    list1.append(num)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if list1[j]>list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
print("Sorted List")
print(list1)