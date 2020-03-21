import json

with open ("vstupne_udaje/map_data_0.json") as file:
    dictionary =json.load(file)


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