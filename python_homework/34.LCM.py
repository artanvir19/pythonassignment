
print("Enter two number: ")
num1=int(input("Number 1: "))
num2=int(input("Number 2: "))

if num1==0 or num2==0:
  print("Enter greater than 0 values")
else:
  if num1<num2:
    greatest = num2
  else:
    greatest =num1
  while True:
    if greatest%num1==0 and greatest%num2==0:
      LCM=greatest
      break
    else:
      greatest+=1
  print(f"The LCM of {num1} and {num2} is {LCM}")

