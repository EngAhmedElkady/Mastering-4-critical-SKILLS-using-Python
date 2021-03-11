# Homework 2: Students grades
f_name=  input("Enter the first student's name : ")
f_ID=int(input("Enter the first student's ID   : "))
f_grade=float(input("Enter the first student's grade   : "))

s_name=  input("\nEnter the second student's name : ")
s_ID=int(input("Enter the second student's ID   : "))
s_grade=float(input("Enter the second student's grade   : "))

print("Informat for students and their \"math\" grades")
print(f_name+"(ID",f_ID,") got grade :",f_grade)
print(s_name+"(ID",s_ID,") got grade :",s_grade)
print("Average math grade is",(f_grade+s_grade)/2)

