#eopi 16.2

def is_valid(col_placement):


def solve_n_queens(n, row, col_placement, result):
    if row == n:
        result.append(col_placement)
        return
    for i in range(n): #for each row
        col_placement.append(i) #test column
        if is_valid(col_placement):

N = 4

result = []
solve_n_queens(N, 0, [], result)