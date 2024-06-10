import math           


# equation of a line
# y = mx+b

def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("This cannot be blank.Please try again.")

        else:
            return response

# dictionaries to hold coordinate details
distance_of_line = []
gradient_of_line = []
midpoint_of_line = []
equation_of_line = []

MAX_coordinates = 1000
coordinates = 0
while coordinates < MAX_coordinates:
    X = not_blank("Please enter the coordinates of your 'X' value or enter"
                  "'xxx' to exit the program.")

    if X == 'xxx'.lower() and len(all(coordinates)) > 0
        break
    elif X == 'xxx'.lower():
        print("")

def line_equation(x1, y1, x2, y2):
    # Calculate the slope (m)
    m = (y2 - y1) / (x2 - x1)


# Calculate the y - intercept (b) using one of the points
b = y1 - m * x1

# Return the equation in slope-intercept form
return f"y = {m}x + {b}"

# Example points
x1, y1 = 2, 3
x2, y2 = 5, 7

# Calculate the equation of the line
equation = line_equation(x1,x2, y2)
print("Equation of the line:",equation)
