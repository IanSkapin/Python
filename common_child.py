from collections import Counter
from random import randint

s1 = 'SHINCHAN'
s2 = 'NOHARAAA'
s3 = 'CABCD'
s4 = 'ABDC'
s5 = 'NCHABNA'
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

"""
NHA
"""


def rand_string(N):
    return "".join([abc[randint(0, 25)] for _ in range(N)])


def find_longest_combination(current_child, i, j, p1, p2):
    c1 = Counter(p1[i:])
    c2 = Counter(p2[j:])
    # traverse both strings while there are matching characters to be added to the child
    while j < len(p2) and i < len(p1):
        if p1[i] == p2[j]:
            # next character matches add it to the child and lets look for the next
            current_child.append(p2[j])
            c1[p1[i]] -= 1
            c2[p2[j]] -= 1
            i += 1
            j += 1
        else:
            # if possible skip characters in the search of the match
            en1 = 0 < c1[p1[i]]
            en2 = 0 < c2[p2[j]]
            if en1 or en2:
                child1 = find_longest_combination(current_child[:], i + 1, j, p1, p2) if en1 else []
                child2 = find_longest_combination(current_child[:], i, j + 1, p1, p2) if en2 else []
                return child1 if len(child1) > len(child2) else child2
            else:
                break
    return current_child

def common_substring(s1, s2):
    l1, l2 = list(s1), list(s2)
    common_genes = set(l1).intersection(set(l2))
    p1 = [x for x in l1 if x in common_genes]
    p2 = [x for x in l2 if x in common_genes]

    longest_child = 0
    # traverse the remaining s1 characters
    for idx1, char in enumerate(p1):
        # find the first matching character in s2
        j = p2.index(char)
        current_child = [p2[j]]
        # count the remaining characters in each string
        i = idx1 + 1
        j += 1
        if longest_child < (current_length := len(find_longest_combination(current_child, i, j, p1, p2))):
            longest_child = current_length
    return longest_child





