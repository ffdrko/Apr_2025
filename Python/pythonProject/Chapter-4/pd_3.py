num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]

print(f"The length of the list is {len(num)}.")
print(num)
num.sort()
print(num)
num.reverse()
print(num)
print(min(num))
print(max(num))

num.append(5)
print(num)

num.insert(5, 20)
print(num)

num.extend([45, 46])
print(num)

num.remove(45)
print(num)
num.pop()
print(num)
num.pop(5)
print(num)

num[0] = 100
print(num)