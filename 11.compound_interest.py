principal=int(input("Enter the principal amonunt: "))
rate=float(input("Enter the rate of interest: "))
time=int(input("Enter the time period in years: "))
compound_interest=principal*pow((1+(rate/100)),time)-principal
print("The compound interest is:",compound_interest)