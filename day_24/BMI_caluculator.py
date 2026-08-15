weight = float(input("Enter your weight in kgs. "))
height = float(input("Enter your height in m. "))

bmi = weight / height ** 2
print("Your BMI score is ", round(bmi, 2))



if bmi < 18.5:
    print("UnderWeight")
elif bmi < 25:
    print("Normal Weight")

else:
    print("OverWeight")
