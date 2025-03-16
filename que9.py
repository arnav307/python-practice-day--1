#3.	Write a python program to calculate BMI of a person when all parameters are provided. BMI= weight(kg)/height(m^2)
height=float(input("Enter your height: "))
weight=float(input("Enter your weight: "))
height=height/100
Bmi=weight/(height**2)
print("Your BMI is ",Bmi)
