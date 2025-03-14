#!/bin/python3

from collections import deque


def transform_to_circles(matrix, m, n):
    """ Extract the circles from the matrix to deques. A frame or circle here is a connected chain of elements starting
    and ending with elements M(i,i). A matrix of dimensions 2x2 has only one circle (its elements being [E(0,0), E(0,1),
    E(1,1), E(1,0)]) and a matrix of dimensions 6x9 has three circles:
        C0 - [E(0,0),...E(0,8),...E(5,8),...E(5,0),...E(1,0)]
        C1 - [E(1,1),...E(1,7),...E(4,7),...E(4,1),...E(2,1)]
        C2 - [E(2,2),...E(2,6),E(3,6),...E(3,2)]

    """
    def of(i, j):
        """Offset: n is length of the line while i and j are matrix/list position indices"""
        # print(f'{i} * {n} + {j} = {i * n + j}')
        return i * n + j

    ar = [x for line in matrix for x in line]
    circles = []
    for k in range(int(min(m, n) / 2)):
        """ Per circle, extract the four sides of frame and create deque.
        frame from matrix = [
            matrix[(k,k):(k,j-k)] + 
            matrix[(k+1,j-k):(i-k-1,j-k)] + 
            matrix[(i-k,j-k):(i-k,k)] + 
            matrix[(i-k-1,k):(k+1,k)]
        ] 
        frame from the matrix line per line concatenation = [
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
    """ Form the matrix of size m,n from the circle deques
    Args:
        circles(list): a list of deques as generated by transform_to_circles
        m(int): number of rows in the in the matrix
        n(int): number of columns in the matrix

    Returns: matrix (list of lists) of dimensions m x n
    """
    matrix = []
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
        matrix.append(ml)
    # print(f'{rotated_matrix}')
    return matrix


def matrix_rotation(matrix, r):
    """ Rotates the given matrix by r in the anti-clockwise direction.
    A matrix rotation by 1 is a move of each element in the matrix by one position in the anti-clockwise direction on its
    frame. A frame or circle here is a connected chain of elements starting and ending with elements M(i,i). A Matrix of
    dimensions 2x2 has only one frame or circle and a matrix of dimensions 6 X 9 has three.

    Args:
        matrix: list if lists of dimensions (m,n) where min(m,n) % 2 = 0
        r: integer representing the number steps each element moves in the anti-clockwise direction

    Returns: a matrix (list of lists) with the elements rotated as per the given r

    """
    m = len(matrix)
    n = len(matrix[0])

    circles = transform_to_circles(matrix, m, n)
    for circle in circles:
        circle.rotate(-(r % len(circle)))  # skip redundant rotations

    return transform_to_matrix(circles, m, n)


