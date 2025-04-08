user_height = int(input("What is your height?: "))

if user_height >= 4:
    print("can ride")
    user_age = int(input("Enter your age: "))
    if user_age <= 12:
        print("Please pay 250 taka.")
    elif user_age <= 18:
        print("Please pay 250 taka.")
    else:
        print("Please pay 500 taka.")
else:
    print("Can't ride.")