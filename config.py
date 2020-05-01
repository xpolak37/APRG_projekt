import json

#nastavenie mapy s prekazkami a cesty

with open("vstupne_udaje/map_data_1.json") as map_file:
    map_dictionary = json.load(map_file)

with open("vstupne_udaje/test_path.json") as path_file:
    path_dictionary = json.load(path_file)
    path_index = 0