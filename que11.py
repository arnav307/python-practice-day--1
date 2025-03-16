#5.	Suppose you are a teacher and you want to create a program that takes in grades from three exams and calculates the average grade for a student. Develop a program to print out the average marks of particular student. 
math=float(input("Enter your marks in math: "))
science=float(input("Enter your marks of science : "))
social=float(input("Enter your marks of social: "))
average_number=(math+science+social)/3
print("The average is ",average_number)