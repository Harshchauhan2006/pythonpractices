#write a program to find out weather the student has passed or failed if it requires total of
#40% and  33 in each subject to pass. Assum 3 subject marks take as an input from the users.

maths=int(input("enter maths marks:- "))
science=int(input("enter science marks:- "))
hindi=int(input("enter hindi marks:- "))

total_percentage=(100*(maths+science+hindi))/300

if(total_percentage>=40 and maths>=33 and science>=33 and hindi>=33):
     print("you are passed:",total_percentage)

else:
     print("you failed try again next year:",total_percentage)