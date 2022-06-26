import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
from math import floor, sqrt, factorial, hypot, log  # log2ないｙｐ
from heapq import heappop, heappush, heappushpop
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from copy import deepcopy
from fractions import gcd
from random import randint


def ceil(a, b): return (a + b - 1) // b


inf = float('inf')
mod = 10 ** 9 + 7


def pprint(*A):
    for a in A:     print(*a, sep='\n')


def INT_(n): return int(n) - 1


def MI(): return map(int, input().split())


def MF(): return map(float, input().split())


def MI_(): return map(INT_, input().split())


def LI(): return list(MI())


def LI_(): return [int(x) - 1 for x in input().split()]


def LF(): return list(MF())


def LIN(n: int): return [I() for _ in range(n)]


def LLIN(n: int): return [LI() for _ in range(n)]


def LLIN_(n: int): return [LI_() for _ in range(n)]


def LLI(): return [list(map(int, l.split())) for l in input()]


def I(): return int(input())


def F(): return float(input())


def ST(): return input().replace('\n', '')


def main():
    N = I()
    P = LI()

    PI = [[0, 0, [], [0] * (N+1)] for _ in range(N+1)]

    for i in range(len(P)):
        PI[i+2][0] = 1 + PI[P[i]][0]
        PI[i+2][1] = P[i]
        PI[P[i]][2].append(i+2)
        PI[i+1][3][0] = 1
    PI.sort(reverse=True)
    for pi in PI:
        for child in pi[2]:
            for i in range(len(PI[child][3])-1):
                pi[3][i+1] += PI[child][3][i]
    print(PI)

    Q = I()
    # for _ in range(Q):


if __name__ == '__main__':
    main()