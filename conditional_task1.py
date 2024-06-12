


#GRADE EVALUATION SYSTEM

s1=float(input("Enter your marks for first subject: "))
s2=float(input("Enter your marks for second subject : "))
s3=float(input("Enter your marks for third subject: "))
s4=float(input("Enter your marks for fourth subject: "))
s5=float(input("Enter your marks for fifth subject: "))

marks=((s1+s2+s3+s4+s5)/500)*100

if (s1<33 or s2<33 or s3<33 or s4<33 or s5<33):
    print("You are failed and hence your grade can not be calculated")
else:

     if (marks>=90):
         print("Your grade is : A")
         print("You are pass and excellent")
     elif(marks>=80 and marks<90):
         print("Your grade is : B")
         print("You are pass and good")
     elif(marks>=70 and marks<80):
         print("Your grade is : C")
         print("You are pass and should work hard")
     elif(marks>=60 and marks<70):
         print("Your grade is : D")
         print("You are pass but needs lots of improvement")
     elif(marks>=50 and marks<60):
         print("Your grade is : E")
         print("You are pass but needs lots of improvement")
     else:
         ("You are fail")


#Weather Suggestion System


name=input("Enter your name please : ")
temp=float(input("Enter the temperature : "))
cond=input("Enter weather condition : ")


if (cond== "sunny"):
    if(temp>30):
        print("Go to beach")
    elif(20<=temp<=30):
        print("Have a picnic ")
    elif(10<=temp<20):
        print("Go for walk")
    elif(temp<10):
        print("Enjoy the sun but wear a jacket")
    else:
        print("Please enter valid input")


elif (cond=="rainy"):
    print("Stay inside and read a book and bring an umbrella if you go out" )


elif(cond=="snowy"):
    if(temp<0):
        print("Go skiing and Wear warm clothes")
    elif(0<=temp<10):
        print("Build a snowman and Wear warm clothes")

    else:
        print("Please enter valid input")

elif(cond=="cloudy"):
    if(10<=temp<20):
        print("Go for a walk")
    elif(temp>=20):
        print("Visit a museum")
    elif(temp<10):
        print("Stay inside and watch movie")
    else:
        print("Please enter valid input")


else:
    print("PLease provide valid inputs!!!")
