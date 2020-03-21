import nacitanie_dat
from matplotlib import pyplot as plt

x_coordinates = nacitanie_dat.x_coordinates()
y_coordinates = nacitanie_dat.y_coordinates()
start_position = nacitanie_dat.start_position()
end_position = nacitanie_dat.end_position()

def graph():
    index = 0
    for i in range (len(x_coordinates)):
        objekt_x = x_coordinates[index]
        objekt_y = y_coordinates[index]
        index = index + 1
        plt.fill(objekt_x, objekt_y, color = "#553B8F",alpha = 0.75)
        plt.scatter(objekt_x,objekt_y, color = "black", s = 20, zorder= 2)


    start_x = start_position[0]
    start_y = start_position[1]
    plt.scatter(start_x, start_y, color = "black", s = 70)

    end_x = end_position[0]
    end_y = end_position[1]
    plt.scatter(end_x, end_y, color = "black", s = 70)
    plt.tight_layout()
    return(plt.show())

