
def minimumBribes(q):
    bribes = [0 for _ in range(len(q))]
    ordered = 0

    def swap(i):
        briber = q[i]
        q[i] = q[i+1]
        q[i+1] = briber
        return briber

    def update_bribes(briber):
        if bribes[briber] >= 2:
            return "Too chaotic"
        bribes[briber] += 1

    def is_briber(j):
        return q[j] > q[j+1]

    while True:
        for idx in range(ordered, len(q)):
            person_idx = q[idx] - 1
            if idx == person_idx:
                ordered = idx
                continue
            if is_briber(idx):
                swap(idx)
                if chaotic := update_bribes(person_idx):
                    return chaotic
                break
        else:
            return sum(bribes)
