list =[]
n =  int(input("Enter the size of list : "))
print("Enter the elements of list : \n")
for i in range(0,n):
    num = int(input())
    list.append(num)
frequency = {}
for i in list:
    if i in frequency:
        frequency[i] +=1
    else:
        frequency[i] = 1
print(frequency)