# BMI Calculator

user_weight = int(input("Enter your weight in kg: "))
user_height = float(input("Enter the height in m: "))

bmi = user_weight / user_height ** 2

if bmi < 18.5:
    print(f"Your bmi is {round(bmi, 2)}. You are underweight.")
elif bmi < 25:
    print(f"Your bmi is {round(bmi, 2)}. You have normal weight.")
elif bmi < 30:
    print(f"Your bmi is {round(bmi, 2)}. You are overweight.")
else:
    print(f"Your bmi is {round(bmi, 2)}. Sorry You have obesity.")