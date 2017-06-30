import csv
import numpy as np

NUM_ACRES_RANGE = (0, 5)
NUM_ROOMS_RANGE = (0, 15)
AVG_ROOM_SIZE_SQ_FT = 200
ROOM_SIZE_VARIANCE = 80

PRICE_PER_SQFT = 1000
PRICE_PER_ROOM = 80000
PRICE_PER_ACRE = 500000
VAR_PER_DOLLAR = 0.30

NUM_SAMPLES = 500

data = []
for i in range(NUM_SAMPLES):
    acreage = np.random.uniform(
        low = NUM_ACRES_RANGE[0], high = NUM_ACRES_RANGE[1]
    )
    num_rooms = np.random.uniform(
        low = NUM_ROOMS_RANGE[0], high = NUM_ROOMS_RANGE[1]
    )
    square_footage = np.random.normal(
        loc = num_rooms * AVG_ROOM_SIZE_SQ_FT,
        scale = num_rooms * ROOM_SIZE_VARIANCE
    )

    price = (
        acreage * PRICE_PER_ACRE
        + square_footage * PRICE_PER_SQFT
        + num_rooms * PRICE_PER_ROOM
    )
    price += np.random.normal(
        scale = price * VAR_PER_DOLLAR
    )

    record = {
        "acreage": acreage,
        "num_rooms": num_rooms,
        "square_footage": square_footage,
        "price": price,
    }

    data.append(record)

with open("data.csv", "w") as f:
    csv_writer = csv.DictWriter(
        f,
        ["acreage", "num_rooms", "square_footage", "price"]
    )

    csv_writer.writeheader()
    for record in data:
        csv_writer.writerow(record)
