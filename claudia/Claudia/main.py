#!/usr/bin/python
import urllib.request
import os
import sys

def read_file(filename):
    if filename.startswith("http"):
        fh = urllib.request.urlopen(filename)
        file_str = fh.read().decode("utf-8")
        return file_str
    else:
        if not os.path.isfile(filename):
            print("file does not exist")
        else:
            file_str = open(filename, "r").read()
            return file_str
file1 = read_file(sys.argv[0])       
# file_str =  
for line in file1:
    if line.start("turn on"):
        line = line.replace(","," ")
        x1 = line.split([2])
        y1 = line.split([3])
        x2 = line.split([5])
        y2 = line.split([6])
        
    elif line.start("turn off"):
        line = line.replace(","," ")
        x1 = line.split([2])
        y1 = line.split([3])
        x2 = line.split([5])
        y2 = line.split([6])
        
    elif line.start("switch"):
        line = line.replace(","," ")
        x1 = line.split([1])
        y1 = line.split([2])
        x2 = line.split([4])
        y2 = line.split([7])
        
def turn_on(self, x1, x2, y1, y2):
    for i in range (y1, y2+1):
        for j in range (x1, x2+1):
            self.a2d[i][j] = 1
        return 
    

