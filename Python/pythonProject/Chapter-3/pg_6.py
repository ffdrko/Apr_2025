user_height = int(input("What is your height?: "))
cost = 0

if user_height >= 4:
    # print("can ride")
    user_age = int(input("Enter your age: "))
    if user_age <= 12:
        cost = 150
    elif user_age <= 18:
        cost = 250
    else:
        cost = 500
else:
    print("Can't ride.")

want_pic = input("do you want photo?: ")

if want_pic == "yes":
    cost = cost + 50
    print(f"Your total bill is {cost}.")
else:
    print(f"Your total bill is {cost}.")