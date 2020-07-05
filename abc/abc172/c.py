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
    N, M, K = MI()
    A = LI()
    B = LI()
    ans = 0
    total = 0
    anow = -1
    for a in A:
        if a + total <= K:
            ans += 1
            total += a
            anow += 1
        else:
            break
    maxans = ans
    for b in B:
        total += b
        isOver = False
        while total > K:
            if anow == -1:
                isOver = True
                break
            total -= A[anow]
            anow -= 1
            ans -= 1
        if isOver:
            break
        ans += 1
        maxans = max(maxans, ans)
    print(maxans)

if __name__ == '__main__':
    main()