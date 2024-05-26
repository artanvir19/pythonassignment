print("Enter the marks for the following subject: ")
math=int(input("Math: "))
phy=int(input("Phy: "))
chem=int(input("Chem: "))
total=math+phy+chem
if (math>=65 and phy>=55 and chem>=50) or total>=180 or (math+phy)>=140:
    print("You are eligible for the professional course.")
else:
    print("You are not eligible for the professional course.")
