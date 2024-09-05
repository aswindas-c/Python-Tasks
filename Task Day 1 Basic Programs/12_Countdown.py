#countdown calculator

def split(date_variable):
    day =""
    month=""
    year=""
    date_list = []
    for j in range(0, 2):
        day = day + date_variable[j]
    date_list.append(int(day))
    for k in range(3,5):
        month = month + date_variable[k]
    date_list.append(int(month))
    for m in range(6,10):
        year = year + date_variable[m]
    date_list.append(int(year))

    return date_list


date1 = input("Enter the date 1 in DD/MM/YYYY format:\n")
date2 = input("Enter the date 2 in DD/MM/YYYY format:\n")

day31 = [1,3,5,7,8,10,12]
day30 = [4,6,9,11]
day28 = [2]

date_list_1 = split(date1)
date_list_2 = split(date2)
day_diff = abs(date_list_2[0] -date_list_1[0])
month_diff = abs(date_list_2[1]  -date_list_1[1])
year_diff = abs(date_list_2[2]-date_list_1[2])

if ((date_list_1[2] > date_list_2[2] and  date_list_1[1] < date_list_2[1]) or
        (date_list_1[2] < date_list_2[2] and  date_list_1[1] > date_list_2[1])):
    year_diff -= 1
    month_diff = 12 - month_diff

if (date_list_1[1] > date_list_2[1] and  date_list_1[0] > date_list_2[0] and date_list_1[2] < date_list_2[2] or
        date_list_1[0] > date_list_2[0] and date_list_1[1] < date_list_2[1] and date_list_1[2] < date_list_2[2]or
        date_list_1[0] < date_list_2[0] and date_list_1[1] > date_list_2[1] and date_list_1[2] > date_list_2[2] or
        date_list_1[1] < date_list_2[1] and  date_list_1[0] < date_list_2[0] and date_list_1[2] > date_list_2[2]):
    month_diff -= 1
    if date_list_2[1] < date_list_1[1]:
        if date_list_2[1] in day31:
            day_diff = 31 - day_diff
        elif date_list_2[1] in day30:
            day_diff = 30 - day_diff
        else:
            day_diff = 28 - day_diff
    else:
        if date_list_1[1] in day31:
            day_diff = 31 - day_diff
        elif date_list_1[1] in day30:
            day_diff = 30 - day_diff
        else:
            day_diff = 28 - day_diff
print(f"Difference is {day_diff} days {month_diff} months and {year_diff} years")
