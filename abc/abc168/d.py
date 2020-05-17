N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] * (N + 1)

dist[1] = 0
q = [1]
while q.__len__():
    now = q.pop(0)
    for i in G[now]:
        if dist[i] == -1:
            q.append(i)
            dist[i] = now

print("Yes")
for i in range(2, N + 1):
    print(dist[i])