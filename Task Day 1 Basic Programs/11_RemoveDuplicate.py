list =[]
n =  int(input("Enter the size of list : "))
print("Enter the elements of list : \n")
for i in range(0,n):
    num = int(input())
    list.append(num)
listnew = []
for i in list:
    if i not in listnew:
        listnew.append(i)
print("List after removing duplicates")
print(listnew)