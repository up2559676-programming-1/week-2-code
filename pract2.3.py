# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from math import pi, sqrt


def int_input(prompt: str) -> int:
    return int(input(prompt))


def speed_calculator():
    distance = int_input("Enter the distance traveled (km): ")
    duration = int_input("Enter the duration of journey (h): ")
    print(f"Speed: {distance / duration}")


def float_input(prompt: str) -> float:
    return float(input(prompt))


def circumference_of_circle():
    radius = float_input("Enter the radius of the circle: ")
    print(f"Circumference: {2 * radius * pi}")


def area_of_circle():
    radius = float_input("Enter the radius of the circle: ")
    print(f"Area: {pi * radius**2}")


def cost_of_pizza():
    pence_per_cm = 3.5

    diameter = float_input("Enter the diameter of the pizza (cm): ")
    area = pi * (diameter / 2) ** 2
    cost = (area * pence_per_cm) / 100
    print(f"Price: £{round(cost)}")


def slope_of_line():
    x1 = float_input("Enter first x coord: ")
    y1 = float_input("Enter first y coord: ")
    x2 = float_input("Enter second x coord: ")
    y2 = float_input("Enter second y coord: ")

    m = float("inf")
    if x2 - x1:
        m = (y2 - y1) / (x2 - x1)

    print(f"Slope: {m}")


def distance_between_points():
    x1 = float_input("Enter first x coord: ")
    y1 = float_input("Enter first y coord: ")
    x2 = float_input("Enter second x coord: ")
    y2 = float_input("Enter second y coord: ")

    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print(f"Distance: {distance}")


def travel_statistics():
    fuel_efficiency = 5

    speed = float_input("Enter the average speed (km/h): ")
    duration = float_input("Enter the duration of journey (h): ")
    distance = speed * duration

    print(f"Distance Traveled: {distance}")
    print(f"Fuel used: {distance / fuel_efficiency} liters")


def sum_of_squares():
    n = int_input("Enter target number (inclusive): ")
    total = 0
    for i in range(1, n + 1):
        total += i**2

    print(f"Total: {total}")


def sum_of_squares_generator():
    n = int_input("Enter target number (inclusive): ")
    total = sum(i**2 for i in range(1, n + 1))
    print(f"Total: {total}")


def average_of_numbers():
    num_of_numbers = int_input("How many numbers are you going to input: ")
    total = 0
    for _ in range(num_of_numbers):
        total += float_input("Enter number: ")

    print(f"Average: {total / num_of_numbers}")


def fibonacci():
    target = int_input("Enter target number: ")
    a, b = 0, 1
    for _ in range(target):
        a, b = b, a + b

    print(f"Value: {a}")


def select_coins():
    pence = int_input("Enter money (pence): ")

    coin_200 = pence // 200
    pence %= 200
    coin_100 = pence // 100
    pence %= 100
    coin_50 = pence // 50
    pence %= 50
    coin_20 = pence // 20
    pence %= 20
    coin_10 = pence // 10
    pence %= 10
    coin_5 = pence // 5
    pence %= 5
    coin_2 = pence // 2
    pence %= 2
    coin_1 = pence // 1

    print(
        f"{coin_200} x £2, {coin_100} x £1, {coin_50} x 50p, {coin_20} x 20p, {coin_10} x 10p, {coin_5} x 5p, {coin_2} x 2p, {coin_1} x 1p"
    )


def select_coins_2():
    coin_names = ["£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p"]
    coins_values = [200, 100, 50, 20, 10, 5, 2, 1]
    coins_quantity = [0] * len(coins_values)

    pence = int_input("Enter money (pence): ")

    for i, coin_value in enumerate(coins_values):
        if pence == 0:
            break

        coins_quantity[i] = pence // coin_value
        pence %= coin_value

    output_parts = [
        f"{quantity} x {name}" for name, quantity in zip(coin_names, coins_quantity)
    ]
    print(", ".join(output_parts))


def select_coins_dict():
    coins = {
        "£2": 200,
        "£1": 100,
        "50p": 50,
        "20p": 20,
        "10p": 10,
        "5p": 5,
        "2p": 2,
        "1p": 1,
    }

    pence = int(input("Enter money (pence): "))

    coins_quantity: dict[str, int] = {}

    for coin_name, coin_value in coins.items():
        if pence == 0:
            break

        coins_quantity[coin_name] = pence // coin_value

        pence %= coin_value

    output_parts = [f"{quantity} x {name}" for name, quantity in coins_quantity.items()]
    print(", ".join(output_parts))


if __name__ == "__main__":
    speed_calculator()
    circumference_of_circle()
    area_of_circle()
    cost_of_pizza()
    slope_of_line()
    distance_between_points()
    travel_statistics()
    sum_of_squares()
    average_of_numbers()
    fibonacci()
    select_coins()
    select_coins_2()
