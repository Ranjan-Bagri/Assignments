def leap_year(year):
	k=str(year)
	if ((k[len(k)-1]==0) and (k[len(k)-2]==0)):
		if (year%400==0):
			return "%s is a leap year"%year
		else:
			return "%s is not a leap year"%year
	else:
		if (year%4==0):
			return "%s is a leap year"%year
		else:
			return "%s is not a leap year"%year

year=int(input('Enter the Year: '))
print(leap_year(year))