principal=int(input("Enter the principal amonunt: "))
rate=float(input("Enter the rate of interest: "))
time=int(input("Enter the time period in years: "))
simple_interest=principal*(rate/100)*time
print("The simple interest is:",simple_interest)