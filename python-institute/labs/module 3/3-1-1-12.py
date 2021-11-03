leap = "Leap year"
common = "Common year"

year = int(input("Enter a year: "))

if year <= 1580:
    output = "Not within the Gregorian calendar period"
elif year % 4 > 0:
    output = common
elif year % 100 > 0:
    output = leap
elif year % 400 > 0:
    output = common
else:
    output = leap

print(output)