"""
Suppose that you have an n-story building (with floors 1 through n) and plenty of eggs. An egg breaks if it is dropped
from floor T or higher and does not break otherwise. Your goal is to devise a strategy to determine the value of T
given the following limitations on the number of eggs and tosses:

    Version 0: 1 egg, ≤T tosses.
    Version 1: ∼1lg n eggs and ∼1lg n tosses.
    Version 2: ∼lg T eggs and ∼2lg T tosses.
    Version 3: 2 eggs and ∼2sqrt(n) tosses.
    Version 4: 2 eggs and ≤c*sqrt(T) tosses for some fixed constant c.

Hints:

    Version 0: sequential search.
    Version 1: binary search.
    Version 2: find an interval containing TTT of size ≤2T\le 2T≤2T, then do binary search.
    Version 3: find an interval of size n\sqrt nn

​, then do sequential search. Note: can be improved to ∼2n tosses.
Version 4: 1+2+3+…+t∼12t2. Aim for c=22c = 2 \sqrt{2}c=22
​.

"""