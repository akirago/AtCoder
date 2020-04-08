K, N = map(int, input().split())
A = [int(n) for n in input().split()]
distances = []
for i in range(N):
    if i == 0:
        distances.append(A[0] + (K - A[N - 1]))
    else:
        distances.append(A[i] - A[i - 1])
distances.sort()
distances.pop(N - 1)
print(summary(distances))
