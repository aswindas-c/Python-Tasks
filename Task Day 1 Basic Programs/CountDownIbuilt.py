from datetime import datetime
from dateutil import relativedelta
date1 = input("Enter first date (DD-MM-YYYY : \n")
date2 = input("Enter second date (DD-MM-YYYY : \n")
date_format = '%d-%m-%Y'
date_object1 = datetime.strptime(date1, date_format)
date_object2 = datetime.strptime(date2, date_format)
diff_date = abs(relativedelta.relativedelta(date_object1,date_object2))
print(f"{diff_date.days} days, {diff_date.months} months, {diff_date.years} years")