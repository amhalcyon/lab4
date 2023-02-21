from datetime import datetime

date1 = "01.01.2015 01:00:00"
date2 = "21.02.2023 22:07:00"
date_1 = datetime.strptime(date1, "%d.%m.%Y %H:%M:%S")
date_2 = datetime.strptime(date2, "%d.%m.%Y %H:%M:%S")
dif = date_2 - date_1

print("Difference between two datetimes in seconds:", dif.total_seconds())