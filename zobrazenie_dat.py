import convex_hull
import optimal_path
import nacitanie_dat
from matplotlib import pyplot as plt

def graph():

    # nakresli jednotlive prekazky
    for i in range(len(x_coordinates)):
        plt.scatter(x_coordinates[i], y_coordinates[i], color="black", s=20, zorder=2)
        plt.fill(x_coordinates[i], y_coordinates[i], color="#553B8F", alpha=0.75)

    # nakresli start a end
    plt.scatter(start_position[0], start_position[1], color="black", s=70)
    plt.scatter(end_position[0], end_position[1], color="black", s=70)

    # nakresli konvexne obalky
    for convex_hull in convex_hulls:
        points_x = []
        points_y = []
        for coordinates in convex_hull:
            points_x.append(coordinates[0])
            points_y.append(coordinates[1])

        plt.scatter(points_x, points_y)
        plt.plot(points_x, points_y, color="orange")

    # nakresli optimalnu cestu
    x_path = []
    y_path = []
    for point in path:
        x_path.append(point[0])
        y_path.append(point[1])

    plt.scatter(x_path, y_path)
    plt.plot(x_path, y_path, "--")

    return plt.show()

convex_hulls = convex_hull.convex_hulls
path = optimal_path.path
x_coordinates = nacitanie_dat.x_coordinates()
y_coordinates = nacitanie_dat.y_coordinates()
start_position = nacitanie_dat.start_position()
end_position = nacitanie_dat.end_position()