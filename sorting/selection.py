"""
public static void sort(Comparable[] a)
{
    int N = a.length;
    for (int i = 0; i < N; i++)
    {
        int min = i;
        for (int j = i+1; j < N; j++)
            if (less(a[j], a[min]))
                min = j;
        exch(a, i, min);
    }
}

"""

from . import exchange


def sort(a):
    # count = 0
    for i in range(len(a)):
        low = i
        for j in range(i + 1, len(a)):
            if a[j] < a[low]:
                low = j
        if low != i:
            exchange(a, i, low)
            # count += 1
    # return count
