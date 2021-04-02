year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    days[1] = 29

result = 0
if month == 1:
    result = day
else:
    for i in range(0, month-1):
        result += days[i]
    result += day

print(result)
