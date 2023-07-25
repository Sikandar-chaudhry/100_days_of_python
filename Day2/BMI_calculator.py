# BMI Calculator 
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weight = float(weight)
height = float(height)

BMI = weight / (height * height)

print(int(BMI))