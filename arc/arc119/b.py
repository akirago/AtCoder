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
    S = input()
    T = input()
    if S.count("1") != T.count("1"):
        print("-1")
        return
    x0 = 0
    x1 = 0
    sb = "s"
    diff = 0
    maxdiff = 0
    ans = 0
    b = ""
    for i in range(N):
        if S[i] != T[i]:
            if S[i] == "1":
                x1 += 1
            else:
                x0 += 1
            if S[i] == "1" and x0 > 0:
                x0 -= 1
                continue
            elif S[i] == "0" and x1 > 0:
                x1 -= 1
                continue
            b = S[i]
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
