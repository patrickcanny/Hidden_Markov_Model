# code adapted from https://stackoverflow.com/questions/17749058/combine-multiple-text-files-into-one-text-file-using-python
import glob
import os

def create_txt(pres='Wilson'):
    exists = os.path.isfile('../data/combined_pres.txt')
    if exists:
        remove_txt()
    read_files = glob.glob('../data/{}{}'.format(pres,'*'))

    with open("combined_pres.txt", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())
    print("file created")
    return

def remove_txt():
    os.remove("combined_pres.txt")
    print("file removed")
    return
