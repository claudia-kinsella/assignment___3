from nose.tools import *
# from src.LEDtester import *
from Claudia.main import *

def test_read_url():
    filename ="http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    eq_(read_file(filename)[:4], "1000", "Files don't match")
     
def test_read_file():
    filename = "../../data/input_assign3.txt"
    eq_(read_file(filename)[:4], "1000", "Files don't match")
     
def test_turn_on():
    ton = led_grid(5)
    ton.turn_on = ("2,3","3,4")
    count = 0
    for i in range(ton.size):
        for j in range(ton.size):
            if ton.grid[i][j] == True:
                count += 1
    eq_(count,4, 'Turn on does not work')
    
def test_turn_off():
    toff = led_grid(5)
    toff.turn_off = ("2,3","3,4")
    count = 0
    for i in range(toff.size):
        for j in range(toff.size):
            if toff.grid[i][j] == True:
                count += 1
    eq_(count,4, 'Turn on does not work')