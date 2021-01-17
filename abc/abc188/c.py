N = int(input())
sNh = 2 ** (N - 1)
A = list(map(int, input().split()))
fA = A[:sNh]
sA = A[sNh:]
print(A.index(min(max(fA), max(sA))) + 1)
