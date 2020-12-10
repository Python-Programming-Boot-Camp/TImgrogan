year = int(input("Enter a year: "))

if year < 1582:
    print("year is out of the Gregorian Calendar range - take a leap!")
elif year % 4 >0:
    print("common year, no division by 4")
elif year % 100 >0:
    print("leap year, no division by 100")
elif year % 400 >0:
    print("common year, no diviosion by 400")
else:
    print("leap year")