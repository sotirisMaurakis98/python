
game_board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

checker = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def row_checker(game_board_array, checker_array):
    for row in game_board_array:
        for index in row:
            if 0 <= index <= 9:
                if index in checker_array and index != 0:
                    checker_array.remove(index)
                elif index not in checker_array and index != 0:
                    return False
            else:
                return False
        checker_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    else:
        return True


def column_checker(game_board_array, checker_array):
    for j in range(0, 9):
        for i in range(0, 9):
            index = game_board_array[i][j]
            if 0 <= index <= 9:
                if index in checker_array \
                        and index != 0:
                    checker_array.remove(index)
                elif index not in checker_array and index != 0:
                    return False
            else:
                return False
        checker_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    else:
        return True


def box_checker(game_board_array, checker_array):
    x = 0
    y = 3
    z = 0
    w = 3
    counter = 0
    while counter < 9:
        for j in range(z, w):
            for i in range(x, y):
                index = game_board_array[i][j]
                if 0 <= index <= 9:
                    if index in checker_array \
                            and index != 0:
                        checker_array.remove(index)
                    elif index not in checker_array and index != 0:
                        return False
                else:
                    return False
        checker_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        counter += 1
        if counter == 3 or counter == 6:
            j = 0
            x += 3
            y += 3
            z = 0
            w = 3
        elif counter < 3:
            i = 0
            x = 0
            y = 3
            z += 3
            w += 3
        elif 3 < counter < 6:
            i = 3
            x = 3
            y = 6
            z += 3
            w += 3
        elif 6 < counter < 9:
            i = 6
            x = 6
            y = 9
            z += 3
            w += 3
    else:
        return True
    
bool1 = column_checker(game_board, checker)
checker = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bool2 = row_checker(game_board, checker)
checker = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bool3 = box_checker(game_board, checker)

if bool1 and bool2 and bool3:
    print("Sudoku solution is correct")
