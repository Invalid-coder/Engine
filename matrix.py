def matrix_multiplication(a, b):
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len(b[0])
    rows_b = len(b)

    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
    if columns_a == rows_b:
        for x in range(rows_a):
            for y in range(columns_b):
                sum = 0
                for k in range(columns_a):
                    sum += a[x][k] * b[k][y]
                result_matrix[x][y] = sum
        return result_matrix

    else:
        print("columns of the first matrix must be equal to the rows of the second matrix")
        return None


def get_vector(a, b):
    return [[b[i][0] - a[i][0]] for i in range(len(a))]


def dot_product(a, b):
    return sum(a[i][0] * b[i][0] for i in range(len(a)))


def cross_product(a, b):
    return [[a[1][0]*b[2][0] - b[1][0]*a[2][0]],
            [b[0][0]*a[2][0] - a[0][0]*b[2][0]],
            [a[0][0]*b[1][0] - b[0][0]*a[1][0]]]


if __name__ == '__main__':
    a = [[1], [2]]
    b = [[2], [2]]
    print(dot_product(a, b))