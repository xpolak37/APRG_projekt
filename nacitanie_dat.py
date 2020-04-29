import config

def map_name():
    """Nacita nazov mapy"""
    map_name = config.map_dictionary["map_name"]
    return map_name

def coordinates():
    """Nacita body vsetkych prekazok"""
    objects = config.map_dictionary["object"]
    coordinates = []
    for object in objects:
        coordinates1 = object["coordinates"]
        coordinates.append(coordinates1)
    return coordinates


def x_coordinates():
    """Nacita x- suradnice bodov prekazok"""
    objects = config.map_dictionary["object"]
    x_coordinates = []
    for object in objects:
        x_coordinates1 = []
        coordinates = object["coordinates"]
        for numbers in coordinates:
            x_coordinate = numbers[0]
            x_coordinates1.append(x_coordinate)

        x_coordinates.append(x_coordinates1)

    return x_coordinates


def y_coordinates():
    """Nacita y- suradnice bodov prekazok"""
    objects = config.map_dictionary["object"]
    y_coordinates = []

    for object in objects:
        y_coordinates1 = []
        coordinates = object["coordinates"]
        for numbers in coordinates:
            y_coordinate = numbers[1]
            y_coordinates1.append(y_coordinate)

        y_coordinates.append(y_coordinates1)

    return y_coordinates


def start_position():
    """Nacita start"""
    paths = config.path_dictionary["path"]
    path_index = config.path_index
    our_path = paths[path_index]
    start_position = our_path["start"]
    return start_position


def end_position():
    """Nacita ciel"""
    paths = config.path_dictionary["path"]
    path_index = config.path_index
    our_path = paths[path_index]
    end_position = our_path["end"]
    return end_position