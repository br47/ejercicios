from Problema0_2 import *

def reset(tarinfo):
    tarinfo.uid = tarinfo.gid = 0
    tarinfo.uname = tarinfo.gname = "root"
    return tarinfo

def createTarfile(tar_file, json_file):
    tar = tarfile.open(tar_file, "w:gz")
    tar.add(json_file, filter=reset)
    tar.close()

def function_1(tar_file):
    tar = readTarfile(tar_file)
    file_name = obtainFileName(tar_file)
    tar.extractall(file_name)
    for tar_content in tar:
        print(tar_content.name)
        if tar_content.name == "metadata.json":
            data = readJSON(file_name + "/" + tar_content.name)
            print(data)
            data['check_name'] = "check_200_modified"
            modifyJSON("metadata_modified.json", data)
            createTarfile("new_blob.tar.gz", "metadata_modified.json")

function_1("./blobs/check_200-2021-08-16T02:46:39.003135.tar.gz")