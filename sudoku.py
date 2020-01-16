# Start writing a method in sudoku solving
import numpy as np
import copy

def get_subgrid(sudoku, i, j):
    """
    return a subgrid from any number in the sudoku grid
    by it's row number i and column number
    """
    i = i//3
    j = j//3
    reference = [(0,3), (3,6), (6,9)]
    return sudoku[reference[i][0]:reference[i][1], reference[j][0]:reference[j][1]]

def newbee_lvl(sudoku):

    for i in range(9): # Column elements
        for j in range(9): # Row elements
            if sudoku[i][j] == 0:
                sub1 = sudoku[i]
                sub2 = sudoku[:, j]
                sub3 = np.reshape(get_subgrid(sudoku, i, j), 9)
                numbers_appeared = np.concatenate((sub1, sub2, sub3))
                sub_all = set(numbers_appeared)
                possible_nums = {1,2,3,4,5,6,7,8,9} - sub_all
                if len(possible_nums) == 1:
                    sudoku[i][j] = list(possible_nums)[0]

def sample():

    easy = np.array([[0,0,0,3,0,9,0,0,5],
                     [5,0,0,0,0,0,1,0,2],
                     [0,0,3,0,4,5,6,0,7],
                     [0,0,0,9,1,8,7,0,3],
                     [1,0,8,0,0,0,9,0,0],
                     [0,2,7,6,3,4,0,0,0],
                     [8,7,1,4,9,0,2,5,6],
                     [0,9,4,2,5,6,0,0,1],
                     [6,5,2,7,8,0,3,0,0]])
    return easy

def newbee_solution(sudoku):

    while True:
        comparison = copy.deepcopy(sudoku)
        newbee_lvl(sudoku)
        if (comparison == sudoku).all():
            print("Simple sudoku fill complete!")
            break
        else:
            print(sudoku)
            print('------------')


if __name__ == '__main__':

    newbee_lvl_sudoku = sample()
    newbee_solution(newbee_lvl_sudoku)
