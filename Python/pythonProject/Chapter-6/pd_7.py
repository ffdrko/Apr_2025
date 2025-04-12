height_input = input("Enter the heights:")
my_list = height_input.split()

suma = 0
count = 0

for i in range(0, len(my_list)):
    my_list[i] = int(my_list[i])
    count +=1

for i in my_list:
    suma += i

avg = suma / count

print(f"The average value is {avg}")