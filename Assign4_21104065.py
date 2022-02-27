##Q1 Tower Of Hanoi
print("Question1")

def tower_of_hanoi(disks, source, auxiliary, target):  
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))  
        return  
    tower_of_hanoi(disks - 1, source, target, auxiliary)  
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))  
    tower_of_hanoi(disks - 1, auxiliary, source, target)  
disks = 3
tower_of_hanoi(disks, 'X', 'Y', 'Z')    #Referring source as X, auxiliary as Y, and target as Z
print("-"*100)
##Q2 Pascals Triangle

print("Question2")

#recursion
p = int(input("Enter number of rows in Pascal's Triangle:"))

print("Using recursion")

def pascals_triangle(n):
    if n == 1:
        return [[1]]
    else:
        result = pascals_triangle(n-1)  #Recursion call
        current_row = [1]
        prev_row = result[-1]
        for i in range(len(prev_row)-1):
            current_row.append(prev_row[i] + prev_row[i+1])
        current_row += [1]
        result.append(current_row)
        return result

triangle = pascals_triangle(p)
for row in triangle:
    print(row)

#iteration

print("Using iteration")

def triangle2(n):
    result = []
    for row in range(n):
        newrow = [1]
        for col in range(1, row+1):
            newcell = newrow[col-1] * float(row+1-col)/col
            newrow.append(int(newcell))
        result.append(newrow)
    return result

triangle = triangle2(p)
for row in triangle:
    print(row)

print("-"*100)
##Q3 2 integer values from user

print("Question3")

input1 = int(input("Please enter the first integer:"))  #user input
input2 = int(input("Please enter the second integer:"))

result = divmod(input1, input2)
#a
print("Pt. A")

print("It's callable") if callable(divmod) else print("It's not callable")
#b
print("Pt. B")

if 0 in [input1, input2] + list(result):
    print("All vaules aren't non-zero.")

elif 0 not in [input1, input2] + list(result):
    print("All the values are non-zero.")
#c
print("Pt. C")

result_list = list(result)

for i in (4, 5, 6):
    result_list.append(i)

filtered_list = []
for j in result_list:   #filtering outt values >4
    if j > 4:
        filtered_list.append(j)

print(f"Filtered out values which are greater than 4 : {filtered_list}")
#d
print("Pt. D")

converted_set = set(filtered_list)  #datatype is converted to set
print(f"Converted Set : {converted_set}")
#e
print("Pt. E")

print("Immutable Set :", frozenset(converted_set))
#f
print("Pt. F")

print("Maximum value :", max(converted_set))    #print the max value
print("Hash value of max value :", hash(max(converted_set)))    # Print the hash value of max value
print("-"*100)
##Q4 create and delete a class

print("Question4")

class Student():
    def __init__(self,name,rollno): #using __init__()
        self.name=name
        self.rollno=rollno
    def f(self):
      print(f"I am {self.name}. My SID is {self.rollno}")
    def __del__(self):  #using __del__()
      print("Object deleted")

person=Student("Amandeep Singh", 21104065)
person.f()
del person  #deleting
print("-"*100)
##Q5 details of 3 employees

print("Question5")

employee_name = str(input("Please enter employee name:\n"))
salary = int(input("Please enter employee's salary\n"))

#creating a dictionary for adding names of employees as key and salaries as value
record_dict = {
     employee_name:salary
}

#while loops for multiple inputs
while (input("Do you want to add details of more employees?Please input Y or N") == "Y"):
    employee_name = str(input("Please enter employee name:\n"))
    salary = int(input("Please enter employee's salary\n"))
    record_dict[employee_name]=salary

print(record_dict)
#a
print("Pt. A")

employee_name = str(input("Please enter employee name:\n"))
new_salary = int(input("Please enter new salary of the employee:"))
new_record = {employee_name:new_salary}
record_dict.update(new_record)
print(record_dict)
#b
print("Pt. B")

del_name = str(input("Please enter name of employee whose record is to be deleted:"))
del record_dict[del_name]
print(record_dict)
print("-"*100)

##Q6 Barbie and George

print("Question6")

george_word = str(input("George's word:"))
def split(word):
    return [char for char in word]

word = george_word
split1= split(word)
split1.sort()
print(split1)

barbie_word = str(input("Barbie's new word:"))
def split(word):
    return [char for char in word]

word = barbie_word
split2= split(word)
split2.sort()
print(split2)

if split1 == split2:
    print("Friendship is real")
else:
    print("Friendship is fake")

print("-*"*50)
