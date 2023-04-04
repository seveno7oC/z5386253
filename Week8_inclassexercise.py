import datetime as dt
#Exercise 13
x = dt.datetime(2023, 12, 31, 9, 30, 33)

s = x.strftime(f'%A of week %U of the year %Y')
print(s)


