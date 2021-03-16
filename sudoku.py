game_board = [
    [8, 1, 2, 7, 5, 3, 6, 4, 9],
    [9, 4, 3, 6, 8, 2, 1, 7, 5],
    [6, 7, 5, 4, 9, 1, 2, 8, 3],
    [1, 5, 4, 2, 3, 7, 8, 9, 6],
    [3, 6, 9, 8, 4, 5, 7, 2, 1],
    [2, 8, 7, 1, 6, 9, 5, 3, 4],
    [5, 2, 1, 9, 7, 4, 3, 6, 8],
    [4, 3, 8, 5, 2, 6, 9, 1, 7],
    [7, 9, 6, 3, 1, 8, 4, 5, 2],
]
checker = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def soduku_checker(checker_array, counter1, counter2):
    variables = [False, False, False]
    for row in game_board:
        for index in row:
            if index in checker_array:
                checker_array.remove(index)
            else:
                print("The given soduku array is wrong")
                exit()
        checker_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    else:
        # print("Row check is all right")
        variables[0] = True

    while counter1 < 9:
        for row in game_board:
            for index in row:
                if index in checker_array and counter2 == 0:
                    checker_array.remove(index)
                    continue
                else:
                    print("The given soduku array is wrong")
                    exit()
            checker_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        counter1 += 1
    else:
        # print("Column check done")
        variables[1] = True

    counter1 = 0
    while counter1 < 9:
        counters = [0, 3, 6]
        for row in game_board:
            for index in row:
                if counter1 in counters:
                    if index in checker_array:
                        checker_array.remove(index)
                    else:
                        print("The given soduku array is wrong")
                        exit()
            checker_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        counter1 += 1
    else:
        # print("Box check done")
        variables[2] = True

    if variables[0] == True and variables[1] == True \
            and variables[2] == True:
        return True
    else:
        return False


if soduku_checker(checker, counter1=0, counter2=0):
    print("The given soduku array is correct")
