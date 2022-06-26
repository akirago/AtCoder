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
    H, W = LI()
    A = [[0] * H] * W
    for h in range(H):
        wl = input()
        for w in range(len(wl) - 1):
            A[h][w] = wl[w]
    B = [[0] * H] * W
    for h in range(H):
        for w in range(W):
            ww = W - w - 1
            hh = H - h - 1
            ad = 0
            if A[ww][hh] == '-':
                ad = -1
            else:
                ad = 1
            if (ww + hh) % 2 == 1:
                ad = ad
            else:
                ad = ad * -1
            if ww == W - 1 and hh == H - 1:
                B[ww][hh] = ad
            elif ww == W - 1:
                print(ad, B[ww][hh + 1])
                B[ww][hh] = ad + B[ww][hh + 1]
                print(B)
            elif hh == H - 1:
                B[ww][hh] = ad + B[ww + 1][hh]
            else:
                if (ww + hh) % 2 == 1:
                    B[ww][hh] = ad + max(B[ww + 1][hh], B[ww][hh + 1])
                else:
                    B[ww][hh] = ad + min(B[ww + 1][hh], B[ww][hh + 1])
    print(B)
    if B[0][0] > 0:
        print("Takahashi")
    elif B[0][0] < 0:
        print("Aoki")
    else:
        print("Draw")


if __name__ == '__main__':
    main()
