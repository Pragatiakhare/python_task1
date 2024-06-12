print("This is the program to calculate BMI of your body")


weight=float(input("Enter your weight in kg: "))

height=float(input("Enter your height in metre: "))

bmi=weight/(height**2)

print("Your BMI is : ",bmi)

if (bmi<18.5):
    print("You are underweight")
elif(bmi>18.5 and bmi<24.9):
    print("Your weight is normal")
elif(bmi>25.0 and bmi<29.9):
    print("You are overweight")
else:
    print("Obese")

print("THANK YOU!!!!!")


