student=[]

num=int(input("Enter number of students: "))
for i in range(num):
 s_name=input("Enter the name of the student: ")
 r_no=int(input("Enter the roll no the student :"))
 marks=float(input("Enter the marks of the student : "))

 tup=(s_name,r_no,marks)
 student.append(tup)
print(student)