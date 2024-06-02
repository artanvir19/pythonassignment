print("Enter two number: ")
num1=int(input("Number 1: "))
num2=int(input("Number 2: "))

if num1==0 or num2==0:
  print("Enter greater than 0 values")
else:
  if num1<num2:
    greatest = num2
  else:
    greatest =num 1
  while True:
    if greatest%num1==0 and greatest%num2==0:
      hcf=greatest
      break
    else:
      greatest+=1
