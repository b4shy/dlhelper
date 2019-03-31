import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
print(myPath)
sys.path.insert(0, myPath + '/../imhelper')

from show import show_images
from read import read_images