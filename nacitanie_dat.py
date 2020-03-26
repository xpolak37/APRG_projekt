import json

with open ("vstupne_udaje/map_data_0.json") as file:
    dictionary =json.load(file)
with open ("vstupne_udaje/test_path.json") as file2:
    dictionary2 = json.load(file2)

path_number = 0

def x_coordinates():
    objects = dictionary["object"]

    x_coordinates = []

    for object in objects:
        x_coordinates1 = []
        coordinates = object["coordinates"]
        for numbers in coordinates:
            x_coordinate = numbers[0]
            x_coordinates1.append(x_coordinate)

        x_coordinates.append(x_coordinates1)

    return(x_coordinates)


def y_coordinates():
    objects = dictionary.pop("object")
    y_coordinates = []

    for object in objects:
        y_coordinates1 = []
        coordinates = object["coordinates"]
        for numbers in coordinates:
            y_coordinate = numbers[1]
            y_coordinates1.append(y_coordinate)

        y_coordinates.append(y_coordinates1)

    return(y_coordinates)

def start_position():
    paths = dictionary2["path"]
    our_path = paths[path_number]
    start_position = our_path["start"]
    return(start_position)


def end_position():
    paths = dictionary2["path"]
    our_path = paths[path_number]
    end_position = our_path["end"]
    return (end_position)