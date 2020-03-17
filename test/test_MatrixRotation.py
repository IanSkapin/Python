import pytest
from .. import MatrixRotation

rotations = [
    [
        [ 1,  2,  3,  4],
        [ 7,  8,  9, 10],
        [13, 14, 15, 16],
        [19, 20, 21, 22],
        [25, 26, 27, 28]
    ],
    [
        [ 2,  3,  4, 10],
        [ 1,  9, 15, 16],
        [ 7,  8, 21, 22],
        [13, 14, 20, 28],
        [19, 25, 26, 27]
    ],
    [
        [ 3,  4, 10, 16],
        [ 2, 15, 21, 22],
        [ 1,  9, 20, 28],
        [ 7,  8, 14, 27],
        [13, 19, 25, 26],
    ],
    [
        [ 4, 10, 16, 22],
        [ 3, 21, 20, 28],
        [ 2, 15, 14, 27],
        [ 1,  9,  8, 26],
        [ 7, 13, 19, 25],
    ],
    [
        [10, 16, 22, 28],
        [ 4, 20, 14, 27],
        [ 3, 21,  8, 26],
        [ 2, 15,  9, 25],
        [ 1,  7, 13, 19],
    ],
    [
        [16, 22, 28, 27],
        [10, 14,  8, 26],
        [ 4, 20,  9, 25],
        [ 3, 21, 15, 19],
        [ 2,  1,  7, 13],
    ],
    [
        [22, 28, 27, 26],
        [16,  8,  9, 25],
        [10, 14, 15, 19],
        [ 4, 20, 21, 13],
        [ 3,  2,  1,  7],
    ],
    [
        [28, 27, 26, 25],
        [22,  9, 15, 19],
        [16,  8, 21, 13],
        [10, 14, 20,  7],
        [ 4,  3,  2,  1],
    ]
]


def get_matrix(i, j):
    return [[int(f'{y}{x}') for x in range(j)] for y in range(i)]


@pytest.mark.parametrize('mat, m, n, reference', [
    (get_matrix(2, 2), 2, 2, [[0, 1, 11, 10]]),
    (get_matrix(2, 3), 2, 3, [[0, 1, 2, 12, 11, 10]]),
    (get_matrix(3, 2), 3, 2, [[0, 1, 11, 21, 20, 10]]),
    (get_matrix(4, 4), 4, 4, [[0, 1, 2, 3, 13, 23, 33, 32, 31, 30, 20, 10], [11, 12, 22, 21]]),
    (get_matrix(6, 6), 6, 6, [[0, 1, 2, 3, 4, 5, 15, 25, 35, 45, 55, 54, 53, 52, 51, 50, 40, 30, 20, 10], [11, 12, 13, 14, 24, 34, 44, 43, 42, 41, 31, 21], [22, 23, 33, 32]]),
    (get_matrix(4, 5), 4, 5, [[0, 1, 2, 3, 4, 14, 24, 34, 33, 32, 31, 30, 20, 10], [11, 12, 13, 23, 22, 21]]),
    (get_matrix(5, 4), 5, 4, [[0, 1, 2, 3, 13, 23, 33, 43, 42, 41, 40, 30, 20, 10], [11, 12, 22, 32, 31, 21]]),
])
def test_transform_to_circles(mat, m, n, reference):
    ref = [MatrixRotation.deque(a) for a in reference]
    output = MatrixRotation.transform_to_circles(mat, m, n)
    for r, o in zip(ref, output):
        assert r == o


@pytest.mark.parametrize('m, n', [(2, 2), (2, 3), (3, 2), (6, 6), (4, 5), (5, 4)])
def test_transform_to_matrix(m, n):
    matrix = get_matrix(m, n)
    reference = MatrixRotation.transform_to_circles(matrix, m, n)
    for k, (r, o) in enumerate(zip(matrix, MatrixRotation.transform_to_matrix(reference, m, n))):
        assert r == o, f'in circle {k} for mat({m}, {n})'



@pytest.mark.parametrize('matrix, rotation, rotated_matrix', [
    (get_matrix(2, 2), 1, [[1, 11], [0, 10]]),
    (get_matrix(2, 2), -1, [[10, 0], [11, 1]]),
    (get_matrix(2, 2), 4, [[0, 1], [10, 11]]),
    (get_matrix(2, 2), -4, [[0, 1], [10, 11]]),
    (get_matrix(2, 2), 0, [[0, 1], [10, 11]]),
    (get_matrix(4, 5), 1, [[1, 2, 3, 4, 14], [0, 12, 13, 23, 24], [10, 11, 21, 22, 34], [20, 30, 31, 32, 33]]),
    (get_matrix(4, 5), 1, [[1, 2, 3, 4, 14], [0, 12, 13, 23, 24], [10, 11, 21, 22, 34], [20, 30, 31, 32, 33]]),
    (rotations[0], 1, rotations[1]),
    (rotations[1], 1, rotations[2]),
    (rotations[0], 7, rotations[7]),
    (rotations[7], -7, rotations[0]),

])
def test_matrix_rotation(matrix, rotation, rotated_matrix):
    assert rotated_matrix == MatrixRotation.matrixRotation(matrix, rotation)

