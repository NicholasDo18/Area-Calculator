import math

print("===================")
print("Area Calculator 📐")
print("===================\n")

print("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n")

shape = int(input("Which shape: "))

if shape == 1:
    base = int(input("\nBase: "))
    height = int(input("Height: "))
    triangle_area = print("\nThe area is " + str((height * base) / 2))
elif shape == 2:
    length = input("length: ")
    width = input("width: ")
    rectangle_area = print("\nThe area is " + str(length * width))
elif shape == 3:
    side = int(input("Side: "))
    square = print("\nThe area is " + str(side ** 2))
elif shape == 4:
    radius = int(input("radius: "))
    circle_area = print("\nThe area is " + str(math.pi * radius ** 2))
elif shape == 5:
    print("\nThank you for using the Area Calculator")
else:
    print("\nInvalid choice")