# BMI Calculator

user_weight = int(input("Enter your weight in kg: "))
user_height = float(input("Enter the height in m: "))

bmi = user_weight / user_height ** 2

print("User BMI is", bmi)