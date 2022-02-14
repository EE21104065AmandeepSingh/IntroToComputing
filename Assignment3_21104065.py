###Q1: counting occurence of each word or character in a string
user_string=str(input("Please enter a string:"))

string_length=len(user_string.split())      #splitting to check if its a string or a single word

#counting if string is entered
if string_length>1:
    words = []
    words = user_string.split()
    freq_words = [words.count(f) for f in words]
    print(dict(zip(words, freq_words)))
    #counting if only 1 word is entered
elif string_length==1:
    frequency={}
    for a in user_string:
        if a in frequency:
            frequency[a]+=1
        else:
            frequency[a]=1
    print("Frequency of each character in the given word is:", str(frequency))
    #output if nothing is entered at all 
else:
    print("Nothing entered to count")
    
###Q2: next date of input date
days31 = [1, 3, 5, 7, 8, 10, 12]        #months with 31 days
days30 = [4, 6, 9, 11]      #months with 30 days
user_date = int(input("Date - \n"))
if 1<=user_date<=31:
    user_month = int(input("Month - \n"))
    if 1<=user_month<=12:
        user_year = int(input("Year - \n"))
        if 1800<=user_year<=2025:
            if user_month in days31:      #31 days 
                if user_month == 12 and user_date == 31:
                    user_year += 1
                    user_month = 1
                    user_date = 1 
                    print("Next date is:", user_date,"/", user_month,"/", user_year)
                elif 1<=user_date<=30:
                    user_date += 1
                    print("Next date is:", user_date,"/", user_month,"/", user_year)
                else:
                    user_date=1
                    user_month+=1
                    print("Next date is:", user_date,"/", user_month,"/", user_year)
            elif user_month in days30:      #30 days
                if 1<=user_date<=29:
                    user_date += 1
                    print("Next date is:", user_date,"/", user_month,"/", user_year)
                else:
                    user_date=1
                    user_month+=1
                    print("Next date is:", user_date,"/", user_month,"/", user_year)
            elif user_month == 2:
                if user_year%4 ==0:
                    if 1<=user_date<=28:
                        user_date += 1
                        print("Next date is:", user_date,"/", user_month,"/", user_year)
                    elif user_date == 29:
                        user_date = 1
                        user_month += 1
                        print("Next date is:", user_date,"/", user_month,"/", user_year)
                    else:
                        print("Leap year February has only 29 days.")
                else:
                    if 1<=user_date<=27:
                        user_date += 1
                        print("Next date is:", user_date,"/", user_month,"/", user_year)
                    else:
                        user_date = 1
                        user_month += 1
                        print("Next date is:", user_date,"/", user_month,"/", user_year)
        else:
            print("Enter year between 1800 and 2025")
    else:
        print("Enter month between 1 and 12")
else:
    print("Enter the date between 1 and 31")
###Q3: to create a list of tuples with 1st element as number and 2nd element as it's square

#taking user input
first_input=int(input("Please enter first number:\n"))  
second_input=int(input("Please enter second number:\n"))
third_input=int(input("Please enter third number:\n"))

#creating tuples
tuple_1=(first_input, first_input**2)
tuple_2=(second_input, second_input**2)
tuple_3=(third_input, third_input**2)
required_list=[tuple_1, tuple_2, tuple_3]

print(required_list)
###Q4: to prompt the user for a grade 

user_input=int(input("Please enter your grade:"))

#because grade can be between 4 to 10, using if-else statements
if 4<=user_input<=10:
    #creating a dictionary as grade:output
    output_dict= {
    10:"Your grade is A+ and it's Outstanding performance.",
    9:"Your grade is A and it's Excellent performance.",
    8:"Your grade is B+ and it's Very Good performance.",
    7:"Your grade is B and it's Good performance.",
    6:"Your grade is C+ and it's Average peformance.",
    5:"Your grade is C and it's Below average performance",
    4:"Your grade is D and it's Poor performance.",
    }
    print(output_dict[user_input])
else:
    print("Please enter a  grade between 4 to 10.")

###Q5: program to print a pattern
lines = 6       #there will be 6 rows of alphabhets
for a in range(lines):
    for b in range(a):
        print(' ', end='')      #spaces in front of alphabets
    for b in range(2*(lines - a)-1):
        print(chr(65+b), end='')        #adding alphabhets
    print()
###Q6: repetedly asks for username and SID    
name_student = str(input("Please enter user name:\n"))
sid_student = int(input("Please enter user's Student ID:\n"))
record_dict = {
     sid_student:name_student
}
while (input("Do you want to add details of more students?Please input Y or N") == "Y"):
    name_student = str(input("Please enter user name:\n"))
    sid_student = int(input("Please enter user's Student ID:\n"))
    record_dict[sid_student]=name_student
print(record_dict)      #a
#b
sorted_value = sorted(record_dict.items(), key = lambda v:v[1])
for w in sorted_value:
    print(w[0], w[1])
#c
print(sorted(record_dict.items()))
#d
inquiry_sid = int(input("Please enter the SID:"))
print(record_dict[inquiry_sid])
###Q7: program to print Fibonacci sequence
#It's not specified if I have to take user input or not, so I am assuming that user input will be taken.
numbers = int(input("Enter the number of terms:"))

first_term = 0
second_term = 1
sum = 0

for Num in range(0, numbers):
    print(first_term, end = '  ')
    sum = sum + first_term
    Next_term = first_term + second_term
    first_term = second_term
    second_term = Next_term

print("\nThe Average of Fibonacci Series is :", sum/numbers)

###Q8: writing python statements on given sets
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
#a
Set4 = Set1.union(Set2)     #All elements in both Set1 and Set2
Set5 = Set1.intersection(Set2)      #Elements common in Set1 and Set2
Set6 = Set4.difference(Set5)
print(Set6)
#b
Set7 = Set1.union(Set2, Set3)       #All elements in the given 3 sets
Set8 = Set1.intersection(Set2)      #Common elements in Set1 and Set2
Set9 = Set2.intersection(Set3)      #Common elements in Set2 and Set3
Set10 = Set3.intersection(Set1)     #Common elements in Set3 and Set1
Set11 = Set8.union(Set9, Set10)     #All common elements
Set12 = Set7.difference(Set11)      #All elements that are only in one of the 3 given sets
print(Set12)
#c
Set13 = Set1.union(Set2, Set3)      #all elements union
Set14 = Set1.intersection(Set2, Set3)       #Elemets common in 3 sets
Set15 = Set1.difference(Set2, Set3)        #Elements only in Set1
Set16 = Set2.difference(Set1, Set3)        #Elements only in Set2
Set17 = Set3.difference(Set1, Set2)        #Elements only in Set3
Set18 = (Set13 - Set14 - Set15 - Set16 - Set17)     #Elements in exactly 2 sets
print(Set18)
#d
Set_int = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}       #integers from 1 to 10
Set19 = Set_int.difference(Set1)        #Integers ranging from 1 to 10 excluding those in Set1
print(Set19)
#e
Set20 = Set_int.difference(Set7)
print(Set20)        #Integers ranging from 1 to 20 not in either of Set1, Set2 or Set3.
