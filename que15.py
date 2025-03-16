#2.	Write a program to calculate in how many days a work will be completed by three persons A, B and C together. A, B, C take x days, y days and z days respectively to do the job alone. The formula to calculate the number of days if they work together is xyz/(xy + yz + xz) days where x, y, and z are given as input to the program.
x=int(input("Enter a person A work: "))
y=int(input("Enter a person B work: "))
z=int(input("Enter a person C work: "))
number_of_days=x*y*z/(x*y+y*z+x*z)
print(f"They need {number_of_days:.2f} days to complete the work")
