sum = 0
for num in range(1,100):
    flag = 0
    for i in range(2, int((num / 2)+1)):
        if num % i == 0:
            flag = 1
    if flag == 0:
        print(num)
        sum = sum + num
print(f"\nSum = {sum}")