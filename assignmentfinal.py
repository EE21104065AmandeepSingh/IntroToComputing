#**************Q1 Finding average of three numbers**************
num1 = int(input("Please enter the first number\n"))
num2 = int(input("Please enter the second number\n"))
num3 = int(input("Please enter the third number\n"))
Average = (num1+num2+num3)/3

print("Average of the inputs is:", Average)
#Avg(a,b,c)=(a+b+c)/3



#**************Q2. Calculating income tax**************
dependents = int(input("Enter the number of dependents\n"))
gross_income = float(input("Enter the income\n"))              #Please enter income in dollars ($). Gross income must be entered to the nearest penny.
taxable_income = float(input("Enter the gross income\n")) #Taxpayer allowed deduction of $3000 per dependent.
income_tax = 0.2*taxable_income                           #All taxpayers are charged a flat tax rate of 20%

print("Your net income tax is:", income_tax)



#**************Q3.To store different data type values into a list.**************
SID = int(input("Enter your SID\n"))
name = input("Enter your name\n")
gender = input("Enter your gender, Use gender values: 'F', 'M', 'U'(unknown)\n")
course_name = input("Enter your course name\n")
CGPA = float(input("Enter CGPA\n"))

student = [SID, name, gender, course_name, CGPA]
print(student)



#**************Q4.program to enter marks of 5 students into a list and display them in sorted manner**************
student1 = int(input("Enter marks of the first student\n"))
student2 = int(input("Enter marks of the second student\n"))
student3 = int(input("Enter marks of the third student\n"))
student4 = int(input("Enter marks of the fourth student\n"))
student5 = int(input("Enter marks of the fifth student\n"))

markslist = [student1, student2, student3, student4, student5]
markslist.sort()
print(markslist)



#**************Q5.**************
color1 = ["Red","Green","White","Black","Pink","Yellow"]
print(color1)

color1.pop(3)
print(color1)

color2 = ["Red","Green", "White", "Black", "Pink", "Yellow"]
color2[3:5]=["Purple"]

print(color2)
