print("Enter two number: ")
num1 = int(input("number1: "))
num2 = int(input("number2: "))

if(num1<=0 or num2<=0):
    print("Invalid input,enter greater than 0")
else:

  if num1>num2:
    smallest = num2
  else:
    smallest = num1

  for i in range (1,smallest+1):
    if (num1%i==0 and num2%i==0):
        hcf = i
  print(f"the HCF of {num1} and {num2} is {hcf}")
  
