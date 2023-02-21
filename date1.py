from datetime import date, timedelta

CurrentDate = date.today()
BeforeDate = CurrentDate - timedelta(5)

print("Current Date:", CurrentDate)
print("Five days from current date:", BeforeDate)