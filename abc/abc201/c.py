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
    S = input()
    o = S.count("o")
    question = S.count("?")
    x = S.count("x")
    if o > 4:
        print(0)
    elif o == 0 and question == 0:
        print(0)
    else:
        ans = 0
        if o + question >= 4:
            if o == 0:
                ans += 24 * question * (question - 1) * (question - 2) * (question - 3)
            elif o == 1:
                ans += 24 * question * (question - 1) * (question - 2)
            elif o == 2:
                ans += 24 * question * (question - 1)
            elif o == 3:
                ans += 24 * question
            elif o >= 4:
                ans += 24
        if o + question >= 3:
            if o == 0:
                ans += 12 * question * (question - 1) * (question - 2) * 3
            elif o == 1:
                ans += 12 * question * (question - 1) * 3
            elif o == 2:
                ans += 12 * question * 3
            elif o == 3:
                ans += 3 * 12
        if o + question >= 2:
            if o == 0:
                ans += (6 + 8) * question * (question - 1)
            elif o == 1:
                ans += (6 + 8) * question
            elif o == 2:
                ans += (6 + 8)

        if o + question >= 1:
            if o == 0:
                ans += question
            if o == 1:
                ans += 1
        print(int(ans))


if __name__ == '__main__':
    main()
