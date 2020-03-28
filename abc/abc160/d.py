N, X, Y = map(int, input().split())
dist = [0]*N
for i in range(1, N):
    for j in range(i+1,N+1):
        a = min(j-i, abs(i-X)+abs(Y-j)+1)
        dist[a] += 1
for i in range(1, N):
    print(dist[i])