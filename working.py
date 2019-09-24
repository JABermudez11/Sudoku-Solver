board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:        # check each num in row if it is equal to num just added
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:        # check each num in column if it is equal to num just added
            return False

    # check 3x3 grid
    box_x = pos[1] // 3     # check which box we are in
    box_y = pos[0] // 3     #

    for i in range(box_y*3, box_y*3 + 3):           # multiply by 3 to be able to get to indices 6,7,8
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:    # again checking if added num already present elsewhere
                return False

    return True


# find empty
def find_empty(bo):

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, col

    return None


print_board(board)
solve(board)
print("_________________________")
print_board(board)