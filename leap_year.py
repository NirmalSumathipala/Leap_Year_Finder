#Taking the year as the user input
year = int(input("Enter the year :"))

#Checking the conditions for a leap year
if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("The year is a leap year.It has 366 days")
        else :
            print("he year is not a leap year.It has 365 days")
    else:
        print("The year is a leap year.It has 366 days")
else :
    print("The year is not a leap year.It has 365 days")