word = input("Enter the string :\n")
reverse = ""
length = 0
for i in word:
    length += 1
for i in range(length-1,-1,-1):
    reverse = reverse + word[i]
print("Reversed String : "+reverse)