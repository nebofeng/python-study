import os

import fnmatch



def findfile(inputdir):

    txtlist = []

    for parent, dirnames, filename in os.walk(inputdir):
        print(filename)
        for filenames in filename:
            txtlist.append(filenames)

    return fnmatch.filter(txtlist, '*.txt')

if __name__ == "__main__":
    findfile("E://")