num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
num3=int(input("Enter the 3rd number: "))

if num1>num2 and num1>num3:
    if num2>num3:
        print(f"the sequenc will be {num1} > {num2} > {num3}")
    else:
        print(f"the sequenc will be {num1} > {num2} > {num3}")
elif num2>num1 and num2>num3:
    if num1>num3:
        print(f"the sequenc will be {num2} > {num1} > {num3}")
    else:
        print(f"the sequenc will be {num2} > {num3} > {num1}")
else:
    if num1>num2:
        print(f"the sequenc will be {num3} > {num1} > {num2}")
    else:
        print(f"the sequenc will be {num3} > {num2} > {num1}")