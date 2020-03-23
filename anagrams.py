
from collections import Counter
from math import factorial


def find_all_the_anagrams(s):
    count = []
    # first we go through all the possible substrings strings
    # i - represents the size of the string and
    # j - its start
    for i in range(1, len(s) + 1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        # count how many times a substring appears
        b = Counter(a)
        # to calculate all the possible combinations (n above r) = n!/r!(n-r)! => where r=2 => n!/(2*(n-2)!)
        count.append(sum([factorial(b[x])/(2 * factorial(b[x] - 2)) for x in b if 1 < x]))
    return sum(count)


