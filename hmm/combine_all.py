# code adapted from https://stackoverflow.com/questions/17749058/combine-multiple-text-files-into-one-text-file-using-python
import glob

read_files = glob.glob('../data/*.txt')

with open("combined_all.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
