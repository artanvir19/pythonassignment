print("Enter two number: ")
num1 = int(input("number1: "))
num2 = int(input("number2: "))

if(num1<=0 or num2<=0):
    print("Invalid input,enter greater than 0")
else:

  if num1<num2:
    greatest = num2
  else:
    greatest = num1
  while True:
     if greatest % num1 == 0 and greatest % num2 == 0:
        lcm=greatest
        break
     else:
        greatest += 1
  print(f"Lcm of {num1} and {num2} is {lcm}")