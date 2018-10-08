import sys
import calendar

def birthday(day, month, year):
	 day = calendar.weekday(year,month,day)
	 if int(day) == 0:
	 	return "You were born on a Monday and Monday's child is fair of face."
	 if int(day) == 1:
	 	return "You were born on a Tuesday and Tuesday's child is full of grace."
	 if int(day) == 2:
	 	return "You were born on a Wednesday and Wednesday's child is full of woe."
	 if int(day) == 3:
	 	return "You were born on a Thursday and Thursday's child has far to go."
	 if int(day) == 4:
	 	return "You were born on a Friday and Friday's child is loving and giving."
	 if int(day) == 5:
	 	return "You were born on a Saturday and Saturday's child works hard for a living."
	 if int(day) == 6:	
	 	return "You were born on a Sunday and Sunday's child is fair and wise and good in every way."


def main():
	day = sys.argv[1]
	month = sys.argv[2]
	year = sys.argv[3]
	birthdays = birthday(int(day), int(month), int(year))
	print(birthdays)

if __name__ == '__main__':
	main()