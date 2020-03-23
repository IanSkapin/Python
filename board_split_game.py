"""
Two HackerRank staffers found a secret room with a mysterious N x N square board and decided to play a game with it. The
game has the following rules:

    At the beginning of the game, the players write a single digit (given as input) ranging from 1 to 9 in each 1 x 1
    cell composing the N x N square board.

    The players move in alternating turns. In each move, the current player performs the following actions:

        1) Chooses a board that has at least one non-prime number written on it and has more than one cell (i.e.,
        dimensions > 1 x 1).

        2) Cuts the chosen board into 2 smaller boards by breaking it along any horizontal or vertical line at the edge
        of a cell.

        Note: Although the game starts with one N x N board, that board is split in two during each move. At the
        beginning of the k**th move, a player can choose any one of the k pieces of the original board (as long as it
        can have a legal move performed on it).

    The game ends when there are no more cuttable boards (i.e., there are N * (1 x 1) boards, or all boards have only
    prime numbers written on them). The first player who is unable to make a move loses.

Given the value of n and the respective numbers written in each (i, j) cell of the board, determine whether the person
who wins the game is the first or second person to move. Assume both players move optimally.

Time Limit

    Python: 18 seconds
    Pypy2: 5 seconds

For other languages, the time limit is standard.

Input Format

The first line contains an integer 'T' denoting the number of test cases.
Each test case is defined as follows over the subsequent lines:

    1) An integer 'N' denoting the length of each of the board's sides.

    2) Each line i of the n subsequent lines contains n space-separated integers describing A(i,0),...A(i,n-1), where
    each A(i,j) describes the number written in cell (i,j) of the board.

Constraints
    1 <= T <= 10
    1 <= N <= 30
    1 <= A(i,j) <= 9

Output Format
    For each test case, print the name of the player with the winning strategy on a new line (i.e., either First or
    Second).

Sample Input

2
3
2 7 5
2 7 5
7 7 7
2
4 3
1 2

Sample Output

Second
First

"""
import numpy

P1 = 'First'
P2 = 'Second'


def next_player(player=None):
    return P2 if player == P1 else P1


def binary_board(board):
    prime_numbers = [2, 3, 5, 7]
    return numpy.array([[x not in prime_numbers for x in line] for line in board])


def can_cut(board):
    if len(board) == 1 and len(board[0]) == 1:
        return False
    return any([any(line) for line in board])


class Stage:
    def __init__(self, boards):
        self.boards = boards

    def next_stage(self):
        for idx, board in enumerate(self.boards):
            if can_cut(board):
                next_boards = [b for i, b in enumerate(self.boards) if i != idx]
                x, y = board.shape
                for i in range(x - 1):
                    yield Stage(next_boards + [board[:i+1,]] + [board[i+1:,]])
                for j in range(y - 1):
                    yield Stage(next_boards + [board[:,:j+1]] + [board[:,j+1:]])


class Cut:
    def __init__(self, stage, player):
        self.player = player
        self.stage = stage
        self.next_cut = None

    def __call__(self):
        """ return the odds of the available cuts"""
        best_odds = None
        total_cuts = even_cuts = odds = 0
        for next_stage in self.stage.next_stage():
            next_cut = Cut(next_stage, next_player(self.player))
            next_total_cuts, next_odd_cuts = next_cut()
            total_cuts += next_total_cuts
            even_cuts += next_total_cuts - next_odd_cuts
            if best_odds is None or next_total_cuts and best_odds < (odds := next_odd_cuts / next_total_cuts):
                best_odds = odds
                self.next_cut = next_cut
        if self.next_cut:
            return total_cuts, even_cuts
        return 1, 1

    def winner(self):
        if not self.next_cut:
            return next_player(self.player)
        if self.next_cut.next_cut:
            return self.next_cut.winner()
        return self.player


def who_wins_on_board(board):
    stage = Stage([binary_board(board)])
    game = Cut(stage, P1)
    game()
    return game.winner()
