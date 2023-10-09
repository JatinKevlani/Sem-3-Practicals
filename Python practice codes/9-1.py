year = int(input("Enter year to find leap year : "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year,"is the leap year")
else:
    print(year,"is not the leap year")