from math import atan2
from math import pi
from collections import deque
from nacitanie_dat import coordinates

def finding_P0(all_coordinates):
    min_y = all_coordinates[0][1]
    x_coordinate = all_coordinates[0][0]
    for coordinates in all_coordinates:
        if coordinates[1] < min_y:
            min_y = coordinates[1]
            x_coordinate = coordinates[0]

    P0 = [x_coordinate, min_y]
    return P0


#zoradenie podla uhlu
def sorting(P0,all_coordinates):
    #vypocet uhlu
    for coordinates in all_coordinates:
        if coordinates[0] < P0[0]:
            dif_x = P0[0] - coordinates[0]
            dif_y = coordinates[1] - P0[1]
            angle = atan2(dif_y,dif_x)
            angle = pi-abs(angle)
        else:
            dif_x = coordinates[0]-P0[0]
            dif_y = coordinates[1]-P0[1]
            angle = atan2(dif_y, dif_x)
        coordinates.append(angle)

    #zoradenie
    x = len(all_coordinates) - 1
    for j in range(x):
        for i in range(x):
            if all_coordinates[i][2] > all_coordinates[i + 1][2]:
                all_coordinates[i], all_coordinates[i + 1] = all_coordinates[i + 1], all_coordinates[i]

    for coordinates in all_coordinates:
        coordinates.pop(2)

    return all_coordinates

def value(list):
    val = (float(list[1][1] - list[2][1]) * (list[0][0] - list[1][0])) - (float(list[1][0] - list[2][0]) * (list[0][1] - list[1][1]))
    return val

#kontrola bodov pomocou zásobníka
def check(points,P0):
    convex_hull = []
    S = deque()
    for i in range(3):
        S.append(points.pop(0))

    index = 0
    while len(points) >= 0:
        a = [] #pomocny zoznam
        for i in range (3):
            a.append(S.pop())

        val = value(a)
        if val < 0:
            S.append(a[2])
            S.append(a[1])
            S.append(a[0])

            if len(points) != 0:
                S.append(points.pop(index))
            else:
                break
        else:
            S.append(a[2])
            S.append(a[0])

    for coordinates in S:
        convex_hull.append(coordinates)

    # kontrola posledného bodu
    S = deque()
    a = []
    x = len(convex_hull)-1
    S.append(convex_hull[x-1])
    S.append(convex_hull[x])
    S.append(convex_hull[0])
    for i in range (3):
        a.append(S.pop())

    val = value(a)
    if not val < 0:
        convex_hull.pop(x)
    convex_hull.append(P0)

    return convex_hull

objects = []
for i in coordinates():
    objects.append(i[:])

convex_hulls = []
for object in objects:
    all_coordinates = object
    #vyhlada P0:
    P0 = finding_P0(all_coordinates)
    # vymaze P0 zo suradnic:
    all_coordinates.remove(P0)
    #zoradi suradnice podla velkosti uhla:
    sorted_coordinates = sorting(P0,all_coordinates)

    #zoradenie vsetkeho do jedneho zoznamu "points"
    points = []
    points.append(P0)
    for coordinates in sorted_coordinates:
        points.append(coordinates)

    #kontrola bodov
    convex_hull = check(points,P0)
    #jednotlive konvexne obalky sa ulozia do zoznamu convex_hulls
    convex_hulls.append(convex_hull)