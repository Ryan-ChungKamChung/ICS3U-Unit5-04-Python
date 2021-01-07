#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in January 2021
# Program finds volume of a cylinder


import math


def volume(radius, height):
    # Function calculates volume and returns it

    # Process and output
    volume = math.pi * (radius ** 2) * height

    return volume


def main():
    # Takes user input, passes it to functions and calls them

    print("Enter a width and radius and I will give",
          " you the volume of a cylinder")

    # Input
    while True:
        # Input
        radius_string = input("Enter radius (cm): ")

        # Process
        try:
            radius = int(radius_string)
            assert radius > 0
            break
        except AssertionError:
            # Output
            print("This isn't a valid input")
        except Exception:
            # Output
            print("This isn't a valid input")
    # Input
    while True:
        # Input
        height_string = input("Enter height (cm): ")

        # Process
        try:
            height = int(height_string)
            assert height > 0
            break
        except AssertionError:
            # Output
            print("This isn't a valid input")
        except Exception:
            # Output
            print("This isn't a valid input")

    # Calls functions
    calculated_volume = volume(radius, height)

    # Output
    # https://stackoverflow.com/questions/
    # 455612/limiting-floats-to-two-decimal-points
    print("The volume of the cylinder is: {:.2f}cm²".
          format(calculated_volume))


if __name__ == "__main__":
    main()
