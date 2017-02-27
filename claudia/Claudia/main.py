import urllib.request
import os
import sys

def read_file(filename="input_assign"):
    if filename.startswith("http"):
        fh = urllib.request.urlopen(filename)
        file_str = fh.read().decode(utf-8)
        return file_str
    else:
        if not os.path.isfile(filename):
           print("file does not exist")
        else:
            file_str = open(filename, "r").read()
            return file_str
        
