row_1 = ["🏠", "🏠", "🏠"]
row_2 = ["🏠", "🏠", "🏠"]
row_3 = ["🏠", "🏠", "🏠"]

matrix = [row_1, row_2, row_3]

print(f'{row_1}\n{row_2}\n{row_3}')

position = input("Enter the position where you want to hide your coin: ")

row = int(position[0])
colum = int(position[1])

row_selected = matrix[row - 1]
row_selected[colum - 1] = "🤑"

print(f'{row_1}\n{row_2}\n{row_3}')