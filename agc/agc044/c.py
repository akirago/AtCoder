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
    n = int(input())
    a = list(map(int, input().split()))
    a = [((i-1)//n, (i-1) % n) for i in a]
    b = [[min(i, n-i-1, j, n-j-1) for j in range(n)] for i in range(n)]
    sit = [[True for j in range(n)] for i in range(n)]
    ans = 0
    for i, j in a:
        sit[i][j] = False
        ans += b[i][j]
        q = [(i, j, b[i][j])]
        while q:
            x, y, z = q.pop()
            if x != 0:
                if b[x-1][y] > z:
                    b[x-1][y] = z
                    q.append((x-1, y, z+sit[x-1][y]))
            if x != n-1:
                if b[x+1][y] > z:
                    b[x+1][y] = z
                    q.append((x+1, y, z+sit[x+1][y]))
            if y != 0:
                if b[x][y-1] > z:
                    b[x][y-1] = z
                    q.append((x, y-1, z+sit[x][y-1]))
            if y != n-1:
                if b[x][y+1] > z:
                    b[x][y+1] = z
                    q.append((x, y+1, z+sit[x][y+1]))
    print(ans)


if __name__ == '__main__':
    main()