my_list = [151, 151, 312, 160, 140]
count = 0
suma = 0

# total_sum_list = sum(my_list)
# avg = total_sum_list / len(my_list)
# print(avg)

for i in my_list:
    suma += i
    count += 1

avg = suma / count

print(avg)