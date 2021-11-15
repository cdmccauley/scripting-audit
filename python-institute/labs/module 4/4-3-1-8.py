def is_year_leap(year):
    if year <= 1580:
        return False
    elif year % 4 > 0:
        return False
    elif year % 100 > 0:
        return True
    elif year % 400 > 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month not in range(1, 13):
        return None
    thirty = [4, 6, 9, 11]
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in thirty:
        return 30
    else:
        return 31

def day_of_year(year, month, day):
    if day > days_in_month(year, month):
        return None
    for i in range(1, month):
        if days_in_month(year, i) != None:
            day += days_in_month(year, i)
        else:
            return None
    return day

print(day_of_year(2000, 12, 31))
