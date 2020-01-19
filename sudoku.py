# Start writing a method in sudoku solving
# Based on a simple 9 * 9 sudoku puzzle with square 3 * 3 subgrids

import numpy as np
import copy

def get_subgrid(sudoku, i, j):
    """
    return a subgrid from any number in the sudoku grid
    by it's row number i and column number j
    """
    i = i//3
    j = j//3
    reference = [(0,3), (3,6), (6,9)]
    return sudoku[reference[i][0]:reference[i][1], reference[j][0]:reference[j][1]]

def int_list2int(int_list):
    list_length = len(int_list)
    init = 0
    for x in range(list_length):
        init += int_list[x]*10**(list_length-1-x)
    return init

def int2int_list(int):
    str_int = str(int)
    return [int(x) for x in str_int]

def newbee_lvl(sudoku):
    """
    This function can only calculate value by numbers' only existence in it's row, column and subgrid.
    So this function can do nothing with values that need assumption.
    """
    fill_nums = 0
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
                    fill_nums += 1

    print("Filled %r numbers in this term."%fill_nums)

def assumption(sudoku):
    
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                sub1 = sudoku[i]
                sub2 = sudoku[:, j]
                sub3 = np.reshape(get_subgrid(sudoku, i, j), 9)
                numbers_appeared = np.concatenate((sub1, sub2, sub3))
                sub_all = set(numbers_appeared)
                possible_nums = {1,2,3,4,5,6,7,8,9} - sub_all
                if len(possible_nums) != 1:
                    sudoku[i][j] = int_list2int(list(possible_nums))
    return sudoku

def assign_only_existance(sudoku):

    for x in range(9):
        for y in soduku[x]:
            if len(y) == 1:
                continue
            else:
                for num in str(y):



def sample(lvl):
    """
    add sample numpy array for test
    """
    if lvl == 'amateur':
        result_array = np.array([[0,0,0,3,0,9,0,0,5],
                                 [5,0,0,0,0,0,1,0,2],
                                 [0,0,3,0,4,5,6,0,7],
                                 [0,0,0,9,1,8,7,0,3],
                                 [1,0,8,0,0,0,9,0,0],
                                 [0,2,7,6,3,4,0,0,0],
                                 [8,7,1,4,9,0,2,5,6],
                                 [0,9,4,2,5,6,0,0,1],
                                 [6,5,2,7,8,0,3,0,0]])
    elif lvl == 'easy':
        result_array = np.array([[0,0,5,0,6,0,0,0,7],
                                 [2,0,0,0,5,0,3,0,0],
                                 [3,0,0,0,2,0,1,0,8],
                                 [1,0,0,7,4,0,9,0,0],
                                 [0,7,0,0,8,0,0,3,0],
                                 [0,0,4,1,0,0,0,0,6],
                                 [6,0,1,0,9,0,0,0,4],
                                 [0,0,3,0,7,0,0,0,5],
                                 [7,0,0,0,1,0,6,0,0]])
    elif lvl == 'medium':
        pass

    elif lvl == 'hard':
        pass

    elif lvl == 'insane':
        pass

    else:
        print("Incorrect level")

    return result_array

def newbee_loop(sudoku):

    while True:
        comparison = copy.deepcopy(sudoku)
        newbee_lvl(sudoku)
        if (comparison == sudoku).all() and (sudoku != 0).all():
            print("Newbee Solution sudoku fill complete!")
            # break
            return sudoku
        elif (comparison == sudoku).all() and (sudoku != 0).any():
            print("Newbee Solution method can do no better!")
            # break
            return sudoku
        else:
            print(sudoku)
            print("%r places still need help"%((sudoku == 0).sum()))
            print('------------')

def main():

    newbee_lvl_sudoku = sample('easy')
    print("Original sudoku:")
    print(newbee_lvl_sudoku)
    print("%r places need help in original sudoku"%((newbee_lvl_sudoku == 0).sum()))
    print("-------------")
    test = newbee_loop(newbee_lvl_sudoku)
    return test
    

def check_only_existance(sudoku, axis):
    if axis == 'row':
        still = copy.deepcopy(sudoku)
        for row in still:
            for y in range(9):
                if len(str(row[y])) != 1:
                    for num in str(row[y]):
                        if num not in ''.join([str(x) for x in row if len(str(x)) > 1 and x != row[y]]):
                            print(num)
                            row[y] = int(num)
                            break
                    else:
                        continue
                    break
            else:
                continue
            break
        return still

    elif axis == 'column':
        still = copy.deepcopy(sudoku.T)
        for column in still:
            for y in range(9):
                if len(str(row[y])) != 1:
                    for num in str(row[y]):
                        if num not in ''.join([str(x) for x in row if len(str(x)) > 1 and x != row[y]]):
                            print(num)
                            row[y] = int(num)
                            break
                    else:
                        continue
                    break
            else:
                continue
            break
        return still.T

    elif axis == 'subgrid':
        still = [np.reshape(sudoku[x[0]:x[1], y[0]:y[1]],9) for x in ((0,3), (3,6), (6,9)) for y in ((0,3), (3,6), (6,9))]
        for subgrid in still:
            for y in range(9):
                if len(str(row[y])) != 1:
                    for num in str(row[y]):
                        if num not in ''.join([str(x) for x in row if len(str(x)) > 1 and x != row[y]]):
                            print(num)
                            row[y] = int(num)
                            break
                    else:
                        continue
                    break
            else:
                continue
            break
        regrid = [np.reshape(x, (3,3)) for x in still]
        return np.concatenate([np.concatenate((regrid[x], regrid[x+1], regrid[x+2]), axis=1) for x in (0,3,6)], axis=0)

    else:
        print("Wrong axis!")


if __name__ == '__main__':
    main()
