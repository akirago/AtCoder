N, M = map(int, input().split())
A = [int(n) for n in input().split()]
A.sort(reverse=True)
total = 0
for x in A:
    total += x
if A[M - 1] / total >= 1 / 4 / M:
    print("Yes")
else:
    print("No")
