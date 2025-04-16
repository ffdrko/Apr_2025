import math
wall_height = int(input("Enter the height of the wall in meters: \n"))
wall_width = int(input("Enter the width of the wall in meters: \n"))

coverage = 7


def paint_cal(height, width, cover):
    area = height * width
    no_of_cans = math.ceil(area/cover)
    print(f"You will need {no_of_cans} cans of paint")


paint_cal(wall_height, wall_width, coverage)