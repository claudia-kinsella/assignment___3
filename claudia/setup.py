'''
Created on 27 Feb 2017

@author: claudiakinsella
'''
from setuptools import setup
setup(name="LED_Assignment3",
      version="0.1",
      description="Assignment 3",
      url="",
      author="Claudia Kinsella",
      author_email="claudia.kinsella@ucdconnect.ie",
      licence="GPL3",
      packages=['Claudia'],
      entry_points={
          'console_scripts':['solve_led=claudia.Claudia.main:main']
          }
      )