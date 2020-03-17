"""
lc = list('asdfkjeghfalawefhaef')
lc = list('bab')



for c in set(lc):
    print(c)
    idx = lc.index(c)
    if i < idx:
        i = idx
        print(i)
"""


def minimal_substring_with_all_elements(s):
    ss_counter = {e: 0 for e in set(list(s))}
    minimal = len(s)
    # i is the tail of the substring and j is the trailing head
    i = j = 0
    while j <= i < len(s):
        while not all(ss_counter.values()) and i < len(s):
            ss_counter[s[i]] += 1
            i += 1
        while all(ss_counter.values()) and j <= i:
            if minimal > (current := sum(ss_counter.values())):
                minimal = current
                position = (j, i)
            ss_counter[s[j]] -= 1
            j += 1
        if minimal == len(ss_counter):
            break
    return minimal, position
