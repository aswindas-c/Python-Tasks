list1 =[]
n =  int(input("Enter the number of rows : "))
m =  int(input("Enter the number of columns : "))
print("Enter the elements of list 1 : \n")
for i in range(0,n):
    list2 = []
    for j in range(0,m):
        num = int(input())
        list2.append(num)
    list1.append(list2)
print(f"2D List : {list1}")

for i in list1:
    sum =0
    for j in i:
        sum = sum + j
    print(f"Sum of Row {i} : {sum}")

print("\n3D list\n")

list3 = [[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]]
for i in list3:
    sum =0
    for j in i:
        for k in j:
            sum = sum + k
    print(f"Sum of Row {i} : {sum}")