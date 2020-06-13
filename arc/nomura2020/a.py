H1, M1, H2, M2, K = map(int, input().split())

total = (H2 - H1) * 60 + M2 - M1
print(total - K)