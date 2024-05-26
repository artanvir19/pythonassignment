num=int(input("Enter the number of subject: "))
def switch(num):
    if num>=90 and num<=100:
        print("A")
    elif num>=87 and num<=89:
        print("B+")
    elif num>=84 and num<=86:
        print("B")
    elif num>=80 and num<=83:
        print("B-")
    elif num>=77 and num<=79:
        print("C+")
    elif num>=74 and num<=76:
        print("C")
    elif num>=70 and num<=73:
        print("C-")
    elif num>=65 and num<=69:
        print("D+")
    elif num>=60 and num<=64:
        print("D")
    elif num>=0 and num<60:
        print("F")
    else:
        print("Invalid input. Please enter value from 0 to 100")

switch(num)
