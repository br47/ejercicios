import tarfile
import json

def readTarfile(tar_file):
    tar = tarfile.open(tar_file, "r:gz")
    return tar

def readJSON(json_file):
    with open(json_file) as file:
        data = json.load(file)
        return data
