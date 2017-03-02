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
    tton=led_grid(5)
    tton.turn_on("2,3","3,4")
    eq_(tton.counter(),4, "test does not work")  
  
def test_turn_off():
    ttoff=led_grid(5)
    ttoff.turn_on("0,4","0,4")
    ttoff.turn_off("2,3","2,4")
    eq_(ttoff.counter(),1, 'test does not work')
      
      
def test_switch():
    tswitch=led_grid(5)
    tswitch.turn_on("0,0","4,4")
    tswitch.switch("1,1","2,2")
    eq_(tswitch.counter(),21, 'test does not work')
    
    