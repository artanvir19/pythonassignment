num=int(input("Enter the nth postion of fibonacci series: "))
n1=0
n2=1
for x in range(1,num+1):
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    