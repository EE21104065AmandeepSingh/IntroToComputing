#############Question1#############


input_string = "Python is a case sensitive language"    #given in the question

#a
print("Length of the input string is: ", len(input_string))

#b
reverse_string = input_string[::-1]
print("Reverse of the input string is: ", reverse_string)

#c
print("New string is: ", input_string[10:-9])   #required string starts after 10th from start and ends at 9th term from end

#d
print(input_string.replace("a case sensitive", "object oriented"))  #replacing  "a case sensitive" with "object oriented" using replace 

#e
print(input_string.index("a"))

#f
print(input_string.replace(" ",""))      #replacing white spaces with void 


#############Question2#############


name_intro = "Hey, ABC Here!"
sid = "My SID is 2110XXXX"
dept_and_cgpa = "I am form XYZ department and my CGPA is 9.9"

student_name = "Amandeep Singh"
student_id = "21104065"
college_dept = "Electrical Engineering"
cgpa = "9.8"

print(name_intro.replace("ABC", student_name))
print(sid.replace("2110XXXX", student_id))
print(dept_and_cgpa.replace("XYZ", college_dept).replace("9.9", cgpa))


#############Question3#############


a = 56  
b = 10  # a and b are given in ques

#a
print(a&b)
#b
print(a|b)
#c
print(a^b)
#d
print(a<<2, b<<2)
#e
print(a>>2, b>>4)


#############Question4#############


num_1 = int(input("Please enter the first number\n"))
num_2 = int(input("Please enter the second number\n"))
num_3 = int(input("Please enter the third number\n"))

numbers = [num_1, num_2, num_3]

a = 0
for num in numbers:
    if (num > a):
        a = num
print(num)


#############Question5#############


user_string = str(input("Please enter a string\n"))

if "name" in user_string:
    print("Yes")
else:
    print("No")


#############Question6#############


side_1 = int(input("Please enter length of first side\n"))
side_2 = int(input("Please enter length of second side\n"))
side_3 = int(input("Please enter length of third side\n"))

if side_1+side_2 > side_3 and side_2+side_3 > side_1 and side_1+side_3 > side_2:
    print("Yes")
else:
    print("No")


###################################