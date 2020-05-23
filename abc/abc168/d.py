import sys

input = sys.stdin.readline
from collections import *


def bfs():
    q = deque([1])
    dist = [0] * (N + 1)
    while q:
        v = q.popleft()

        for nv in G[v]:
            if dist[nv] == 0:
                dist[nv] = v
                q.append(nv)

    return dist


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = bfs()

print("Yes")
for i in range(2, N + 1):
    print(dist[i])
