# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import math


def float_input(prompt: str) -> float:
    return float(input(prompt))


def square_dimensions():
    square_size = 100

    x = float_input("Enter the x coordinate of the top-left corner: ")
    y = float_input("Enter the y coordinate of the top-left corner: ")

    print(f"Top-left coordinates: {x}, {y}")
    print(f"Top-right coordinates: {x + square_size}, {y + square_size}")


def square_dimensions_full():
    square_size = 100

    x = float_input("Enter the x coordinate of the top-left corner: ")
    y = float_input("Enter the y coordinate of the top-left corner: ")

    print(f"Top-left coordinates: {x}, {y}")
    print(f"Top-right coordinates: {x + square_size}, {y}")
    print(f"Bottom-left coordinates: {x}, {y + square_size}")
    print(f"Bottom-right coordinates: {x + square_size}, {y + square_size}")


def rectangle_boundaries():
    rect_size = (100, 100)

    x = float_input("Enter the x coordinate of the top-left corner: ")
    y = float_input("Enter the y coordinate of the top-left corner: ")

    print(f"X range: {x}, {x + rect_size[0]}")
    print(f"Y range: {y}, {y + rect_size[1]}")


def circle_circumference():
    radius = 50

    x = float_input("Enter the x coordinate of the center: ")
    y = float_input("Enter the y coordinate of the center: ")

    print(f"The circumference is {2 * math.pi * radius}")


def circle_metrics():
    radius = 50

    x = float_input("Enter the x coordinate of the center: ")
    y = float_input("Enter the y coordinate of the center: ")

    print(f"The circumference is {2 * math.pi * radius}")
    print(f"The area is {math.pi * radius**2}")


def distance_between_points():
    x1 = float_input("Enter the x coordinate of the first point: ")
    y1 = float_input("Enter the y coordinate of the first point: ")
    x2 = float_input("Enter the x coordinate of the second point: ")
    y2 = float_input("Enter the y coordinate of the second point: ")

    print(
        f"The distance between the points is {math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)}"
    )


if __name__ == "__main__":
    square_dimensions()
    square_dimensions_full()
    rectangle_boundaries()
    circle_circumference()
    circle_metrics()
    distance_between_points()
