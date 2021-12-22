def direction(facing, turn):
    compass = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    turn //= 45
    start_index = compass.index(facing)
    new_index = (start_index + turn) % len(compass)

    return compass[new_index]