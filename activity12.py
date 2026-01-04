height = float(input("enter your height in cm:"))
weight = float(input("enter your weight in kg:"))

bmi = weight / (height/100)**2
print("your bmi is",bmi)

if bmi <= 18.4:
    print("you are underweight")
elif bmi <= 24.9:
    print("you are healthy")
elif bmi <= 29.9:
    print("you are overweight")
elif bmi <= 34.9:
    print("you are obese")
else:
    print("you are severely obese")