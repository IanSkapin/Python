"""

public static void sort(Comparable[] a)
{
    int N = a.length;
    for (int i = 0; i < N; i++)
        for (int j = i; j > 0; j--)
            if (less(a[j], a[j-1]))
                exch(a, j, j-1);
            else break;
}

"""

from . import exchange


def sort(a: list, lo: int = None, hi: int = None):
    lo = lo or 0
    size = hi + 1 or len(a)
    for i in range(size):
        for j in range(i, lo, -1):
            if a[j] < a[j - 1]:
                exchange(a, j, j - 1)
            else:
                break
