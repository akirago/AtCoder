import numpy as np

s = input()[::-1]
length = len(s)
t = np.zeros(length, dtype=int)
dp = np.zeros(2019, dtype=int)

x = 1
mod = 2019
t[0] = s[0]
dp[t[0]] = 1
print("i=", 0, t[0])

for i in range(1, length):
    x = (x * 10) % mod
    t[i] += (x * int(s[i]) + t[i - 1]) % mod
    print("i=", i, t[i])
    dp[t[i]] += 1
    print(t[i], dp[t[[i]]])

ans = 0
for i in dp:
    ans += i * (i - 1) // 2

print(ans)
