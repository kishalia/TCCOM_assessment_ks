def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("ERROR!Please answer yes or no.")


def show_instructions():
    print('''\n
    ***** INSTRUCTIONS *****

Please enter...

- The coordinates of :
  Your "X" value
  Your "Y" value

Select the information you would like to work out:
- Distance
- Gradient
- Midpoint
- Equation of a line

Once you have selected what information you would like to input, press enter.
The distance, gradient, midpoint and equation of a line will be displayed.

The information will be written to a text file.

  **************************''')


# main routine goes here

while True:
    show_instructions() = yes_no("Would you like instructions? ").lower()
    if show_instructions() == "yes" or show_instructions() == "y":
        print(show_instructions())
