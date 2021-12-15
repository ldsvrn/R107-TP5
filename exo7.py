import os
import datetime

path = input("1. Entrez un path: ")
path2 = input("2. Entrez un path: ")

def fileInfo(path):
    if not os.path.isfile(path):
        raise Exception(f"Le fichier {path} n'existe pas!")

    milis = os.path.getmtime(path)
    print(f"Le fichier {path} ({os.path.getsize(path)} octets) à été modifié le "
          f"{datetime.datetime.fromtimestamp(milis)} (unix milis: {milis})")


fileInfo(path)
fileInfo(path2)
