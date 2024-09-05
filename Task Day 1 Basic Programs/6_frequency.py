number_list =[]
try:
    n =  int(input("Enter the size of list : "))
    print("Enter the elements of list : \n")
    for i in range(0,n):
        num = input()
        number_list.append(num)
    frequency = {}
    for i in number_list:
        if i in frequency:
            frequency[i] +=1
        else:
            frequency[i] = 1
    print(frequency)
except ValueError:
    print("Enter Integer Value")