import json
import zobrazenie_dat

with open("vstupne_udaje/map_data_1.json") as map_file:  # toto skusit dat prec dat do config file
    map_dictionary = json.load(map_file)

with open("vstupne_udaje/test_path.json") as path_file:
    path_dictionary = json.load(path_file)
    path_index = 0

def main():
    zobrazenie_dat.graph()

if __name__ == "__main__":
    main()