""""""


def compress(S):
    comp = []
    e_old = S[0]
    cnt = 0
    for e in S:
        if e != e_old:
            comp.append([cnt, e_old])
            e_old = e
            cnt = 1
        else:
            cnt += 1
    comp.append([cnt, e_old])
    return comp


def length_compressed(comp):
    length = 0
    for cnt, e in comp:
        length += 1 + (len(str(cnt)) if cnt > 1 else 0)
    return length


def fix_compressed(comp, remove, K):
    updated = []
    for idx, (cnt, e) in enumerate(comp):
        if idx == remove:
            K -= cnt
            if K > 0:
                remove += 1
            elif K < 0:
                if updated and updated[-1][1] == e:
                    updated[-1][0] += -K
                else:
                    updated.append([-K, e])
            continue
        if updated and updated[-1][1] == e:
            updated[-1][0] += cnt
        else:
            updated.append([cnt, e])
    return updated


def solution(S, K):
    # write your code in Python 3.6
    s = compress(S)
    shortest = len(S)
    for idx, (cnt, e) in enumerate(s):
        if cnt <= K or len(str(cnt)) > len(str(cnt - K)):
            ss = fix_compressed(s, idx, K)
            lss = length_compressed(ss)
            if shortest > lss:
                shortest = lss
    return shortest