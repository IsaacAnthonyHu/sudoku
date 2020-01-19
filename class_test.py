# Try to initiate a class about sudoku

import numpy as np
import copy

class Sudoku():
    
    def __init__(self, np_array):
        self.columns = [np_array[:,i] for i in range(9)]
        self.rows = [np_array[i] for i in range(9)]
        self.subgrids = [[np_array[y[0]:y[1],x[0]:x[1]] for x in [(0,3), (3,6), (6,9)]] for y in [(0,3), (3,6), (6,9)]]
