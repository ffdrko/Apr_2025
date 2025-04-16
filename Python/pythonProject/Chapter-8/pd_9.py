# local scope
def addition(xx, yx):
    return xx+yx


result = addition(10, 20)
print(result)

x = 40
y = 30


def sub(a=x, b=y):
    return a-b


result_1 = sub()
print(f"{x}and {y}")