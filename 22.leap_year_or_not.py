year=int(input("Enter a year: "))
if year%400==0:
 print("It is a leap year")
elif year%100!=0 and year%4==0:
 print("It is a leap year")
else:
 print("It is not a leap year")