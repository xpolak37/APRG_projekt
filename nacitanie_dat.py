import json

with open ("vstupne_udaje/map_data_0.json") as file:
    dictionary =json.load(file)

objects = dictionary.pop("object")
x_coordinates1 = []
y_coordinates1 = []
x_coordinates = []
y_coordinates = []

for object in objects:
    coordinates = object["coordinates"]
    for numbers in coordinates:
        x_coordinate = numbers[0]
        y_coordinate = numbers[1]
        x_coordinates1.append(x_coordinate)
        y_coordinates1.append(y_coordinate)

    x_coordinates.append(x_coordinates1)
    y_coordinates.append(y_coordinates1)

print(x_coordinates)
print(y_coordinates)