board = [
    [0, 3, 1, 0, 0, 0, 8, 6, 0],
    [8, 5, 0, 7, 2, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 6, 0, 0, 0],
    [5, 0, 8, 6, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 4, 5, 0, 3],
    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 7, 3, 0, 2, 6],
    [0, 9, 3, 0, 0, 0, 7, 5, 0]
]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
    return None


def valid(board, value, pos):
    # Checking row
    for i in range(len(board)):
        if board[pos[0]][i] == value and i != pos[1]:
            return False

    # checking column
    for i in range(len(board)):
        if board[i][pos[1]] == value and i != pos[0]:
            return False

    # checking box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == value and (i, j) != pos:
                return False

    return True


def solve(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(board, i, (row,col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

if __name__ == '__main__':
    print_board(board)
    solve(board)
    print("")
    print_board(board)