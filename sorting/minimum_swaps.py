""" sort the array using minimal swaps and return their count """
from . import exchange


def sort(arr: list):
    count = 0
    for i in range(0, len(arr)):
        while arr[i] != i + 1:
            exchange(arr, arr[i] - 1, i)
            count += 1
    return count
