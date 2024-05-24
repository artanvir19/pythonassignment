n=int(input("Enter a number: "))
s=0

#if it start from begining
for x in range(2,n+1,2):
 s+=x
print(f"the sum fo even numbers from 0 to {n} is",s) 
