temp=float(input("Enter the centigrade temperature: " ))

def switch(temp):
    if temp < 0:
        print("Freezing weather")
    elif temp<10:
        print("Very cold weather")
    elif temp<20:
        print("Cold weather")
    elif temp<30:
        print("Normal in temp")
    elif temp<40:
        print("Hot weather")
    elif temp>=40:
        print("it's very hot weather")
    else:
        print("Invalid Input")
switch(temp)        