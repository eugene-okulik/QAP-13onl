import datetime

print(datetime.datetime.now())

date_now = datetime.datetime.now()
print(date_now.second)

my_date = datetime.datetime(2024, 12, 5)
print(my_date.day)
my_date_str = 'Apr 18 20:52:09'
parsed_date = datetime.datetime.strptime(my_date_str, '%b %d %H:%M:%S')
parsed_date = parsed_date.replace(year=2023)
print(parsed_date)
print(parsed_date.strftime('%b %d, %A - %H:%M:%S'))
