def is_valid(board, row, col, n):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_queen(board, col, n):
    if col == n:
        return True
    
    for row in range(n):
        if is_valid(board, row, col, n):
            board[col] = row
            if solve_queen(board, col + 1, n):
                return True
            board[col] = -1

    return False

def print_board(board, n):
    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()

def solve_n_queens(n):
    board = [-1] * n
    if solve_queen(board, 0, n):
        print_board(board, n)
    else:
        print('No solution found')
print(solve_n_queens(8))