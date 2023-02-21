import datetime

CurrentDate = datetime.datetime.now()
CurrentDate = CurrentDate.replace(microsecond=0)

print(CurrentDate)