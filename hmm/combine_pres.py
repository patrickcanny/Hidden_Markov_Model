# code adapted from https://stackoverflow.com/questions/17749058/combine-multiple-text-files-into-one-text-file-using-python
import glob

pres = 'Wilson'
read_files = glob.glob('../data/{}{}'.format(pres,'*'))

with open("combined_pres.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
