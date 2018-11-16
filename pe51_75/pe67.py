import networkx as nx
import numpy as np

import sys
sys.path.append('..')
from pe01_25.pe18 import *

"""
Problem:
https://projecteuler.net/problem=67

Find the maximum total from top to bottom of the triangle (see pe67.txt)

Solution:
Use the shortest path algorithm from pe18.py.

"""
L = [l.split(" ") for l in open("pe51_75\pe67.txt", "r").read().splitlines()]
trianglelist = [[-int(x) for x in l] for l in L]

print(maxpathsum(trianglelist))
