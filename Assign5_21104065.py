#Amandeep Singh
#SID:21104065 - ELECTRICAL ENGINEERING
#Assignment 5 (Optional)
##########Q1##########
from tkinter import*

def gst():
  org_cost=int(org_entry.get())
  net_cost=int(net_entry.get())

  #applying the formula
  gst_output=((net_cost-org_cost)*100)/org_cost;

  #inserting the output in the entry
  gst_entry.insert(10,str(gst_output)+"%")

if __name__ == "__main__":
  win=Tk()
  win.title("GST tax finder")
  win.geometry("700x500")

  #labels
  original_price=Label(win,text="Enter original price:")
  net_price=Label(win,text="Enter net price:")
  gst_rate=Label(win,text="Calculated GST rate:")
  #Calculate button
  calculate=Button(win,text="Calculate",command=gst)

  #positioning labels and button
  original_price.place(x=10,y=10)
  net_price.place(x=10,y=60)
  gst_rate.place(x=10,y=170)
  calculate.place(x=200,y=110)

  #entry
  org_entry=Entry(win)
  net_entry=Entry(win)
  gst_entry=Entry(win)

  #positioning Entry
  org_entry.place(x=150,y=10)
  net_entry.place(x=150,y=60)
  gst_entry.place(x=150,y=170)
win.mainloop()
##########Q2##########
from tkinter import*
import calendar

def cal_output():
  new_cal=Tk()
  new_cal.title("Calendar Output")
  new_cal.geometry("500x650")
  
  #taking user input
  get_year=int(year_entry.get())

  #fetching result from calendar library
  cal_content=calendar.calendar(get_year)

  #output
  final_output=Label(new_cal, text=cal_content)

  #poistioning
  final_output.place(x=10,y=10)

  new_cal.mainloop()

if __name__=="__main__":

  cal=Tk()
  cal.title("CALENDAR")
  cal.geometry("300x150")

  #adding labels
  cal_label=Label(cal,text="Calendar By Year")
  enter_year=Label(cal,text="Enter the Year")
  
  #user year entry
  year_entry=Entry(cal)

  #Button
  show=Button(cal,text="Show",command=cal_output)

  #positioning labels, entry and button
  cal_label.place(x=10,y=20)
  enter_year.place(x=10,y=40)
  year_entry.place(x=10,y=60)
  show.place(x=10,y=100)

  cal.mainloop()
##########Q3##########
from tkinter import*

#for addition
def addition():
  add_num1=int(first_entry.get())
  add_num2=int(second_entry.get())

  add_result=(add_num1+add_num2);

  result_entry.insert(10, str(add_result))

#for substraction
def substraction():
  sub_num1=int(first_entry.get())
  sub_num2=int(second_entry.get())

  sub_result=sub_num1-sub_num2;

  result_entry.insert(10, str(sub_result))

#for division
def division():
  div_num1=int(first_entry.get())
  div_num2=int(second_entry.get())

  div_result=div_num1/div_num2;

  result_entry.insert(10, str(div_result))

#for multlipication
def multiplication():
  mul_num1=int(first_entry.get())
  mul_num2=int(second_entry.get())

  mul_result=mul_num1*mul_num2;

  result_entry.insert(10, str(mul_result))

if __name__=="__main__":
  calc=Tk()
  calc.title("Simple Calculator")
  calc.geometry("350x350")

  #Labels
  first_number=Label(calc,text="First Number")
  second_number=Label(calc, text="Second Number")
  result=Label(calc, text="Answer")

  #Entries
  first_entry=Entry(calc)
  second_entry=Entry(calc)
  result_entry=Entry(calc)

  #buttons
  add_button=Button(calc,text="+",command=addition)
  sub_button=Button(calc,text="-",command=substraction)
  div_button=Button(calc,text="/",command=division)
  mul_button=Button(calc,text="*",command=multiplication)

  #placing labels, entries and buttons
  first_number.place(x=10,y=10)
  second_number.place(x=10,y=50)
  first_entry.place(x=150,y=10)
  second_entry.place(x=150,y=50)
  add_button.place(x=75,y=80)
  sub_button.place(x=150,y=80)
  div_button.place(x=75,y=130)
  mul_button.place(x=150,y=130)
  result.place(x=10,y=180)
  result_entry.place(x=150,y=180)

  calc.mainloop()
##########Q4##########
def qsort(marks):
    if len(marks) <= 1:
        return marks
    else:
       return qsort([x for x in marks[1:] if x < marks[0]]) + [marks[0]] + qsort([x for x in marks[1:] if x >= marks[0]])
    
if __name__=="__main__":

  marks=[]

  #given is question that n is number of students
  n=int(input("Enter the number of students:"))

  for i in range(0,n):
    user_input=int(input("Enter the marks:"))
    marks.append(user_input)
  print(qsort(marks))
##########Q5##########
def qsort(marks):
    if len(marks) <= 1:
        return marks
    else:
       return qsort([x for x in marks[1:] if x < marks[0]]) + [marks[0]] + qsort([x for x in marks[1:] if x >= marks[0]])
    
def binary_search(list,low,high,x):
     if low<=high :
        mid=(high+low)//2
        if list[mid]==x:
            return mid
        elif list[mid]>x:
            return binary_search(list,low,mid-1,x)
        else:
            return binary_search(list,mid+1,high,x)

def CountFrequency(list):
 
    # Creating an empty dictionary
    freq = {}
    for item in list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("% d : % d"%(key, value))

if __name__=="__main__":

  list=[]

  #n is the number of numbers to be entered
  n=int(input("Enter how many numbers you want ot enter:"))

  for i in range(0,n):
    user_input=int(input("Enter the number:"))
    list.append(user_input)
  print(qsort(list))    #a

  x=int(input("Find the integer you want to find:"))
  #c
  if x in list:
    print(CountFrequency(x))     
  else:
    print("ERROR: Number not in the list")