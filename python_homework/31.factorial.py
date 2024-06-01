num=int(input("Enter the number you want to know the factorial: "))
fact=1
for i in range (1,num+1):
    fact=fact*i
print(f"The factorial of {num} is: {fact}")
