my_set = {18, 56, 89, "Bangladesh", False}
print(my_set)
my_set1 = set()
print(my_set1, type(my_set1))

my_set1.add(99)
print(my_set1)
my_set.remove(False)
print(my_set)
my_set.discard(False)
print(my_set)
x = my_set.pop()
print(my_set)
print(x)