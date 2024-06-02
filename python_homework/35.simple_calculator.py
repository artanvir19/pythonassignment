def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

print("Chose what kind of operation you want to do:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation =(input("Enter your choice(1,2,3,4): "))
if operation in ("1","2","3","4"):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if operation == "1":
        print(num1,"+",num2,"=",add(num1,num2))
    elif operation == "2":
        print(num1,"-",num2,"=",sub(num1,num2))
    elif operation == "3":
        print(num1,"*",num2,"=",multi(num1,num2))
    elif operation == "4":
        if(num2!=0):
          print(num1,"/",num2,"=",div(num1,num2))
        else:
            print("You can't divide by zero")
else:
    print("Invalid choice")
