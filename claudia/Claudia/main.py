import urllib.request
import os
import sys
from numpy.core.defchararray import startswith
from pip._vendor.pyparsing import replaceWith
 
def read_file(filename):
    """Function to read a file and process the contents"""
    if filename.startswith("http"):
        file_h = urllib.request.urlopen(filename)
        file_line=file_h.read().decode('utf-8')
        return file_line
    else:
        if not os.path.isfile(filename):
            print('File does not exist.')
        else:
        # Open the file for reading as a string
            file_line = open(filename, 'r').read()
            return file_line 
            
        
def main():
    """Function to make a matrix"""
#     file_str = read_file('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt')
#     first_line = int(file_str.splitlines()[0])
#     file_line=read_file("../../data/input_assign3.txt")
#     file_line = read_file('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b_v2.txt')
    file_line = read_file(sys.argv[2])
   
    lines = file_line.split('\n')
    size = int(lines[0])
    array = led_grid(size)
    
    for line in lines:
        
#         if ' ,' in line:
#             line.replace(' ,',',')
#         if ', ' in line:
#             line.replace(', ',',')
        if 'turn on' in line or ' turn on' in line:
            a,b,c,d,e = line.split(" ")
            array.turn_on (c,e)
        elif "turn off" in line or ' turn off' in line:
            a,b,c,d,e = line.split(" ")
            array.turn_off (c,e)
        elif "switch" in line or ' switch' in line:
            a,b,c,d = line.split(" ")
            array.switch (b,d)
        else:
            pass
    
class led_grid():
     
    def __init__(self, S): 
        self.size= S 
        self.grid = [[False]*S for _ in range(S)]
          
