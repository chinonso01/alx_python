def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for coloum in row:
            print("{:d} ".format(coloum), end="")
        print()