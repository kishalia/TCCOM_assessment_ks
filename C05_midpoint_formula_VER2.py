n = int(input("Enter the number of points: "))

sum_x = 0
sum_y = 0

for i in range(n):
    x = int(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1}: "))
    sum_x += x
    sum_y += y

xm = sum_x / n
ym = sum_y / n

midpoint = (xm, ym)
print(f"The midpoint of the shape is: {midpoint}")
