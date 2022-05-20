import random
import itertools
from collections import Iterable


def generate_1d_matrix(y):
    return [random.randint(0, 9) for _ in range(y)]


def generate_3d_matrix(i, j, k):
    return [[[random.randint(0, 9) for col in range(k)]for row in range(j)] for x in range(i)]


def convert_3d_to_1d(matrix):
    for val in matrix:
        if isinstance(val, Iterable):
            yield from convert_3d_to_1d(val)
        else:
            yield val


def convert_1d_to_3d(matrix, i, j, k):
    counter = itertools.count().__next__
    return [[[matrix[counter()]for col in range(k)]for row in range(j)] for x in range(i)]


def main():
    matrix_1d = generate_1d_matrix(27)
    print('1D Matrix:\n', matrix_1d)

    matrix_3d_converted = convert_1d_to_3d(matrix_1d, 3, 3, 3)
    print('1D to 3D Matrix Conversion:\n', matrix_3d_converted, '\n')

    matrix_3d = generate_3d_matrix(3, 3, 3)
    print('3D Matrix:\n', matrix_3d)

    matrix_1d_converted = list(convert_3d_to_1d(matrix_3d))
    print('3D to 1D Matrix Conversion:\n', matrix_1d_converted, '\n')


if __name__ == '__main__':
    main()
