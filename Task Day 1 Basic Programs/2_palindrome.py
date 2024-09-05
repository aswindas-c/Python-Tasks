word = input("Enter the string :\n")
length=0
flag = 0
for i in word:
    length += 1
j=length-1
for i in range(0,int(length/2)):
    if word[i] != word[j]:
        flag = 1
        break
    j=j-1
if flag == 0:
    print(word + " is palindrome")
else:
    print(word + " is not a palindrome")