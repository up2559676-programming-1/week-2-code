# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import math


def float_input(prompt: str) -> float:
    return float(input(prompt))


def painted_wall():
    paint_cover = 2000
    tin_cost = 12.0

    length = float_input("Enter the length (cm) of the wall: ")
    h = float_input("Enter the height (cm) of the wall: ")
    w = float_input("Enter the width (cm) of the window: ")
    y = float_input("Enter the height (cm) of the window: ")

    total_area = length * h
    window_area = w * y
    wall_area = total_area - window_area
    tin_req = math.ceil(wall_area / paint_cover)
    cost = tin_req * tin_cost

    print(f"The total wall area is {total_area} cm².")
    print(f"The window area is {window_area} cm².")
    print(f"The paintable wall area (excluding the window) is {wall_area} cm².")
    print(f"The number of tins required is {tin_req}.")
    print(f"The total cost of paint is £{round(cost, 2)}.")


def garden_lawn():
    seeds_kg_per_meters = 0.3
    seed_bag_kg = 20

    s = float_input("Enter the side length of the garden (m): ")
    p = float_input("Enter the width of the gravel path (m): ")

    total_garden_area = s**2
    lawn_area = (s - p) ** 2
    path_area = total_garden_area - lawn_area
    grass_seed = lawn_area * seeds_kg_per_meters

    print(f"The total garden area (square) is {total_garden_area}m².")
    print(f"The lawn area without the path (square) is {lawn_area}m².")
    print(f"The path area (rectangular border) is {path_area}m².")
    print(f"The total amount of grass seed required is {grass_seed} kg.")
    print(
        f"The number of bags of seed required is {math.ceil(grass_seed / seed_bag_kg)}."
    )


def swimming_pool():
    tile_size = 0.25
    tile_cost = 2
    budget = 1500

    length = float_input("Enter the length of the pool (m): ")
    w = float_input("Enter the width of the pool (m): ")
    b = float_input("Enter the border width of tiling (m): ")

    total_area = (length + b) * (w + b)
    pool_area = length * w
    tile_area = total_area - pool_area
    tiles = math.ceil(tile_area / tile_size)
    tiles_cost = tiles * tile_cost

    print(
        f"The total area of the pool plus the rectangular border is {(length + b) * (w + b)}m²."
    )
    print(f"The area of the pool alone (rectangle) is {pool_area}m².")
    print(f"The tiled border area (rectangle ring) is {tile_area}m².")
    print(f"The number of square tiles required for the border is {tiles}.")
    print(f"he cost of the tiles is £{tile_cost}.")
    print(
        f"The maximum number of full pools that can be tiled with the £1500 budget is {int(budget / tiles_cost)}."
    )


def solar_farm():
    req_border = 1
    panel_output = 400
    run_time = 30

    length = float_input("Length of the field (m): ")
    w = float_input("Width of the field (m): ")
    l_panel = float_input("Length of one panel (m): ")
    w_panel = float_input("Width of one panel (m): ")

    total_field_area = length * w
    effective_panel_area = (l_panel + req_border) * (w_panel + req_border)
    num_panels = int(total_field_area / effective_panel_area)
    daily_output = num_panels * panel_output
    monthly_output = daily_output * run_time

    print(f"The total field area (rectangle) is {total_field_area}m².")
    print(
        f"The effective area of one panel including its rectangular spacing border is {effective_panel_area}m²."
    )
    print(
        f"The maximum number of full panels (rectangles) that can fit into the field is {num_panels}."
    )
    print(f"The daily energy output of the farm is {daily_output} kWh.")
    print(f"The monthly energy output of the farm is {monthly_output} kWh.")


def int_input(prompt: str) -> int:
    return int(input(prompt))


def cinema_seating():
    refurbish_cost = 250.0
    ticket_cost = 7.0
    refurbish_budget = 10_000.0

    r = int_input("Number of rows in the cinema: ")
    c = int_input("Number of seats per row: ")

    total_num_seats = r * c
    max_revenue = total_num_seats * ticket_cost
    total_refurbish = total_num_seats * refurbish_cost
    refurbish_amount = int(refurbish_budget / refurbish_cost)
    refurbish_num_rows = int(refurbish_amount / c)

    print(f"The total number of rectangular seats in the cinema is {total_num_seats}.")
    print(
        f"The revenue if all rectangular seats are sold for one showing is £{max_revenue}"
    )
    print(f"The total cost to refurbish all rectangular seats is £{total_refurbish}.")
    print(
        f"The number of rectangular seats that can be refurbished with the £10,000 budget is {refurbish_amount}."
    )
    print(
        f"The number of full rows of rectangular seats that can be refurbished with the £10,000 budget is {refurbish_num_rows}."
    )


if __name__ == "__main__":
    painted_wall()
    garden_lawn()
    swimming_pool()
    solar_farm()
    cinema_seating()
