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
    N = int(input())
    A = list(input().rstrip())
    def two_num(x):
        res = 0
        while x % 2 == 0:
            x //= 2
            res += 1
        return res

    C_twos = [0] * N
    for i in range(1, N):
        res = C_twos[i - 1] + two_num(N - i) - two_num(i)
        C_twos[i] = res

    if '2' in A:
        ans = 0
        for i in range(N):
            ans ^= (int(A[i]) - 1) & 1 * (C_twos[i] == 0)
        print(ans)
    else:
        ans = 0
        for i in range(N):
            ans ^= (int(A[i]) - 1) // 2 * (C_twos[i] == 0)
        print(ans * 2)


if __name__ == '__main__':
    main()