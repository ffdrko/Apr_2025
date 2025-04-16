# def mul(x, y):
#     return x*y
#
#
# print(mul(2, 5))

def mul(*num):
    multi = 1
    for i in num:
        multi *= i
    return multi


print(mul(2.4, 4.5, 5.7))