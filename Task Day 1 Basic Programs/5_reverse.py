str = input("Enter the string :\n")
reverse = ""
length = 0
for i in str:
    length += 1
for i in range(length-1,-1,-1):
    reverse = reverse + str[i]
print("Reversed String : "+reverse)