N, K = map(int, input().split())
A = [int(i) for i in input().split()]

loop_count = 0
loop = [0] * N
i = 1
town = A[0] - 1
loop[0] = i
if N > K:
    for _ in range(K - 1):
        town = A[town] - 1
    print(town + 1)
else:
    while True:
        if loop[town] == 0:
            i += 1
            loop[town] = i
            town = A[town] - 1
        else:
            break
    loop_size = i - loop[town] + 1

    if loop_size != 0:
        K = (K - i) % loop_size

    for _ in range(K):
        town = A[town] - 1

    print(town + 1)
