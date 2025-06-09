def sum_primary_diagonal(matrix):

    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total


def sum_secondary_diagonal(matrix):

    total = 0
    n = len(matrix)
    for i in range(n):
        total += matrix[i][n - 1 - i]
    return total

