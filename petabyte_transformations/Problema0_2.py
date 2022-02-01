from Problema0_1 import *

import os

def modifyJSON(json_file, data):
    with open(json_file, "w") as jsonFile:
        json.dump(data, jsonFile)
        print(data)

def obtainFileName(file):
    return (os.path.splitext(os.path.splitext(file)[0])[0])
