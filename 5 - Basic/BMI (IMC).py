#BMI = weight in kgs / (height in m)^2
weight = float(input("Enter wight in kgs: "))
height = float(input("Enter height in meters: "))

bmi = weight/height**2

print(f"BMI is {bmi}")