# app/core/constants.py

PARK_COORDINATES = {
    "bottom_left": (55.736431, 37.331806),
    "top_right": (55.811328, 37.449476)
}

def is_within_park(latitude: float, longitude: float) -> bool:
    return (PARK_COORDINATES["bottom_left"][0] <= latitude <= PARK_COORDINATES["top_right"][0] and
            PARK_COORDINATES["bottom_left"][1] <= longitude <= PARK_COORDINATES["top_right"][1])
