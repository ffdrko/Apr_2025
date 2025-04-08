print("1.small_size_pizza_price = Tk100")
print("2.medium_size_pizza_price = Tk200")
print("3.large_size_pizza_price = Tk300")

user_order = int(input("Enter your pizza size: "))

total_bill = 0

small_size_pizza_price = 100
medium_size_pizza_price = 200
large_size_pizza_price = 300

pepperoni_small = 30
pepperoni_med_lar = 50

extra_chess = 20

if user_order == 1:
    total_bill = small_size_pizza_price

    user_order_extra = input("you want pepperoni?: yes or no: ")
    user_order_cheese = input("you want cheese?: yes or no: ")

    if user_order_extra == 'yes':
        total_bill = total_bill + pepperoni_small
    if user_order_cheese == 'yes':
        total_bill = total_bill + extra_chess
elif user_order == 2:
    total_bill = medium_size_pizza_price

    user_order_extra = input("you want pepperoni?: yes or no: ")
    user_order_cheese = input("you want cheese?: yes or no: ")

    if user_order_extra == 'yes':
        total_bill = total_bill + pepperoni_med_lar
    if user_order_cheese == 'yes':
        total_bill = total_bill + extra_chess
else:
    total_bill = large_size_pizza_price

    user_order_extra = input("you want pepperoni?: yes or no: ")
    user_order_cheese = input("you want cheese?: yes or no: ")

    if user_order_extra == 'yes':
        total_bill = total_bill + pepperoni_med_lar
    if user_order_cheese == 'yes':
        total_bill = total_bill + extra_chess

print(f"Your total bill is {total_bill}")