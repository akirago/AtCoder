N = int(input())
k_has = [[] for _ in range(N)]
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    k_has[a].append(b)
    k_has[b].append(a)
for k in range(N):
    used = [False for _ in range(N)]
    used[k] = True
    choices = {k}
    while choices.__sizeof__() != 0:
        choices.remove()
