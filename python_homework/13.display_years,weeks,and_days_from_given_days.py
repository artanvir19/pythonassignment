days=int(input("Enter the number of days: "))
year=days//365
month=(days%365)//30
days=((days%365)%30)
print(f"There will be {year} year, {month} month, {days} days")