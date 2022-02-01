from Problema0_1 import *
from Problema0_2 import obtainFileName

def function_2(tar_file, checkname):
    tar = readTarfile(tar_file)
    file_name = obtainFileName(tar_file)
    tar.extractall(file_name)
    for tar_content in tar:
        data = readJSON(file_name + "/" + tar_content.name)
        if data['check_name'] == checkname:
            print(tar_content)

function_2("new_blob.tar.gz", "check_200_modified")