import datetime

from datetime import date

print("Date")
print(date.today().weekday())
print(date.today().__str__())
print(date.today().strftime("%d/%m/%Y"))
print(date.fromordinal(7899))
# print(date.fromisoformat(""))

print("Datetime")
print(datetime.datetime.today())
print(datetime.datetime.today().time())
print(datetime.datetime.today().strftime("%d/%m/%Y %H"))
# print(datetime.datetime.fromisoformat(""))

from datetime import timedelta

print("Timedelta")
five_min_delta = timedelta(minutes=5)
print(datetime.timedelta(minutes=5, seconds=45))
print(datetime.datetime.today().__add__(five_min_delta))
print(datetime.datetime.today().__sub__(five_min_delta))

print(datetime.time.minute)
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
