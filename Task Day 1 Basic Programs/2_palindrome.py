str = input("Enter the string :\n")
length=0
flag = 0
for i in str:
    length += 1
j=length-1
for i in range(0,int(length/2)):
    if str[i] != str[j]:
        flag = 1
        break
    j=j-1
if flag == 0:
    print(str + " is palindrome")
else:
    print(str + " is not a palindrome")