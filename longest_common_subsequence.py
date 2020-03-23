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

# ----------------------------------------------------------


def lcs_length_matrix(str1, str2):
    M = [x[:] for x in [[0]*(len(str1) + 1)]*(len(str2) + 1)]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                M[i+1][j+1] = M[i][j] + 1
            else:
                M[i+1][j+1] = max(M[i][j+1], M[i+1][j])
    return M


def lcs_length_trimmed(string1, string2):
    start = 0
    end = 0
    end1 = len(string1) - 1
    end2 = len(string2) - 1
    while start <= end1 and start <= end2 and string1[start] == string2[start]:
        start += 1
    while start <= end1 and start <= end2 and string1[end1-end] == string2[end2-end]:
        end += 1
    core = lcs_length(string1[start:end1], string2[start:end2])
    return start + core + end


def lcs_length(str1, str2):
    previous = [0]*(len(str1) + 1)
    for i in range(len(str1)):
        current = [0]*(len(str2) + 1)
        for j in range(len(str2)):
            current[j + 1] = previous[j] + 1 if str1[i] == str2[j] else max(previous[j+1], current[j])
        previous = current[:]
    return previous[-1]


# ------------------------------------------------

def sort_with_index(string):
    return sorted(range(len(string)), key=lambda x: string[x])


def active_indices(string1, string2):
    idx1 = sort_with_index(string1)
    idx2 = sort_with_index(string2)
    start = 0
    R = [[] for _ in range(len(string1))]
    old_char = ''
    for i_idx, i in enumerate(idx1):
        if old_char == (char := string1[i]):
            R[i] = R[idx1[i_idx - 1]]
            continue
        for j_idx, j in enumerate(idx2[start:]):
            if char != string2[j]:
                next_start = start + j_idx
                break
            R[i].append(j)
        R[i] = sorted(R[i], reverse=True)
        if char != old_char:
            old_char = char
            start = next_start
    return R

from sorting.priority_queue import BinaryHeap

def lcs_length_optimized(str1, str2):
    R = active_indices(str1, str2)
    T = BinaryHeap(mode='min')
    T.insert(0)
    for i in range(len(str1)):
        for j in R[i]:
            pass # TODO


