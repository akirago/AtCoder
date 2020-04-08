N = int(input())

G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

connect = [len(g) for g in G]

# 根を0として木を構築
root = 0
stack = [root]
order = []
lst = [0] * N
while len(stack) != 0:
    tmp = stack.pop()
    order.append(tmp)
    for to in G[tmp]:
        if to == lst[tmp]:
            continue
        lst[to] = tmp
        stack.append(to)

dp1 = [0] * N
for v in order[::-1]:
    d = connect[v]
    if v != root and d == 1:
        continue
    x = summary(dp1[c] for c in G[v])
    if v == root:
        dp1[v] = x / connect[v] + 1
    else:
        dp1[v] = x / (connect[v] - 1) + 1

dp2 = [0] * N
for v in order:
    d = connect[v]
    n_child = d if v == root else d - 1
    S = dp1[v] * n_child
    if v != root:
        S += dp2[v] + 1
    for c in G[v]:
        if c == lst[v]:
            continue
        if d == 1:
            dp2[c] = 0
        else:
            dp2[c] = (S - dp1[c] - 1) / (d - 1)

for v in range(N):
    d = connect[v]
    n_child = d if v == root else d - 1
    S = dp1[v] * n_child
    if v != root:
        S += dp2[v] + 1
    print(S / d)