full_mark=int(input("Enter the full mark :"))
bangla=int(input("Enter marks of Bangla: "))

English=int(input("Enter marks of English: "))
Math=int(input("Enter marks of Math: "))
Science=int(input("Enter marks of Science: "))
Islam=int(input("Enter marks of Islam: "))
total=bangla+English+Math+Science+Islam
average=total/5
print("\n")
print("Total Marks:",total)
print("\n")
print("Average Marks:",average)
print("\n")
print("Percentage in Bangla",(bangla*100)/full_mark,"\nPercentage in English",(English*100)/full_mark,"\nPercentage in Math",(Math*100)/full_mark,"\nPercentage in Science",(Science*100)/full_mark,"\nPercentage in ",(Islam*100)/full_mark)