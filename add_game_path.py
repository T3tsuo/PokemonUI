import os
import pickle

if not os.path.isfile("game_path.dat"):
    path = input("Enter PokeMMO folder path (ex 'C:\Program Files\PokeMMO'): ").replace("\\", "/") + "/config"
    pickle.dump(path, open("game_path.dat", "wb"))
