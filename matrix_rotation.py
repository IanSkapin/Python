#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


def transform_to_circles(matrix, m, n):
    """ extract the circles from the matrix to deques """

    def of(i, j):
        """OFfset: n is length of the line while i and j are matrix/list position """
        # print(f'{i} * {n} + {j} = {i * n + j}')
        return i * n + j

    ar = [x for line in matrix for x in line]
    circles = []
    for k in range(int(min(m, n) / 2)):
        """ 
        circle: [matrix[(k,k):(k,j-k)] + matrix[(k+1,j-k):(i-k-1,j-k)] + 
                 matrix[(i-k,j-k):(i-k,k)] + matrix[(i-k-1,k):(k+1,k)] =
        [
            ar[of(k,k):of(k,(n-1)-k)] + 
            [ar[of(i,(n-1)-k)] for i in range(k+1, (m-1)-k-1)] +
            ar[of((m-1)-k, (n-1)-k):of((m-1)-k, k):-1] + 
            [ar[of(i, k)] for i in range((m-1)-k-1), k+1)]
        ]
        """
        # print(f'k:{k}')
        top = ar[of(k, k):of(k, n - k)]
        # print(f'{top}')
        right = [ar[of(i, n - 1 - k)] for i in range(k + 1, m - k - 1)]
        # print(f'{right}')
        bottom = ar[of(m - 1 - k, n - 1 - k):of(m - 1 - k, k) - 1: -1]
        # print(f'{bottom}')
        left = [ar[of(i, k)] for i in range(m - 1 - k - 1, k, -1)]
        # print(f'{left}')
        circles.append(deque(
            top +
            right +
            bottom +
            left
        ))
    return circles


def transform_to_matrix(circles, m, n):
    """ form the matrix from the circle deques """
    rotated_matrix = []
    for i in range(m):
        ml = []  # matrix line
        for j in range(n):
            if i > j and j < n / 2 and i < m - 1 - j:
                # print(""" left quarter of the matrix """)
                ml.append(circles[j].pop())
            elif i <= j and i <= n - 1 - j and i < m / 2:
                # print(""" top quarter of the matrix """)
                ml.append(circles[i].popleft())
            elif m - 1 - i <= j and m - 1 - i <= n - 1 - j:
                # print(""" bottom quarter of the matrix """)
                ml.append(circles[m - i - 1].pop())
            elif i > n - j - 1 and j >= n / 2 and i < m - 1 - (n - 1 - j):
                # print(""" right qarter of the matrix """)
                ml.append(circles[n - j - 1].popleft())
            else:
                raise Exception(f'Error {i},{j} is out of bounds')
            # print(f'({i},{j}) ml={ml}')
        rotated_matrix.append(ml)
    # print(f'{rotated_matrix}')
    return rotated_matrix


# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])

    circles = transform_to_circles(matrix, m, n)
    for circle in circles:
        circle.rotate(-(r % len(circle)))  # skip redundant rotations

    matrix = transform_to_matrix(circles, m, n)
    # for l in matrix:
    #    print(' '.join(map(str, l)))
    return matrix


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)