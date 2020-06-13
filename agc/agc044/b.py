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
    P = MI()
    emp = [[1] * (N + 1) for _ in range(N + 1)]
    dp = [[inf] * (N + 1) for _ in range(N + 1)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            ax = min(x - 1, N - x)
            ay = min(y - 1, N - y)
            dp[x][y] = min(ax, ay)
    ans = 0
    for i in P:
        y = (i % N)
        x = (i // N) + 1
        if y == 0:
            y += N
            x -= 1
        ans += dp[x][y]
        emp[x][y] = 0
        q = {(x, y)}
        while q:
            now = q.pop()
            for j in range(len(dx)):
                nx = now[0] + dx[j]
                ny = now[1] + dy[j]
                if 1 <= nx <= N and 1 <= ny <= N and dp[nx][ny] == dp[now[0]][now[1]] + 1 + emp[now[0]][now[1]]:
                    dp[nx][ny] -= 1
                    q.add((nx, ny))
    print(ans)


if __name__ == '__main__':
    main()
