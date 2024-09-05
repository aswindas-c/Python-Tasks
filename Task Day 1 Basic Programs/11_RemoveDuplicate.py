list1 =[]
try:
    n =  int(input("Enter the size of list : "))
    print("Enter the elements of list : \n")
    for i in range(0,n):
        num = input()
        list1.append(num)
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    print("List after removing duplicates")
    print(list2)
except ValueError:
    print("Enter Integer Value")