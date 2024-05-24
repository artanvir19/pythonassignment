print("Enter three angle of a triangle")
angle1=int(input("angle1: "))
angle2=int(input("angle2: "))
angle3=int(input("angle3: "))

if(angle1+angle2+angle3)==180:
    print("Triangle is valid")
else:
    print("Triangle is not valid")