from nose.tools import *
# from src.LEDtester import *
from Claudia.main import *
from Claudia.main import read_file

def test_read_url():
    filename ="http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    eq_(read_file(filename)[:4], "1000", "Files don't match")
    
def test_read_file():
    filename = "../data/input_assign3.txt"
    eq_(read_file(filename)[:4], "1000", "Files don't match")