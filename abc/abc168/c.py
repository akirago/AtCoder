import math
A, B, H, M = map(int, input().split())

kakuA = 30 * H + 30 * M / 60
kakuB = 360 * M / 60

dkaku = abs(kakuA - kakuB)
dkaku = min(dkaku, 360 - dkaku)
print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(dkaku))))