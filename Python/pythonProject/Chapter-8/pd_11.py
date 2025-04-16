user_num = int(input("Enter your num: "))


def prime_num(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False

    if flag:
        print("Number is a prime number")
    else:
        print("Number is not a prime number")


prime_num(user_num)