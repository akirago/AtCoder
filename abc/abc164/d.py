import collections

S = "1234"
Sint = int(S)
i = 1
ans = 0
dp = [0 for _ in range(2019)]
at = 0
for x in range(len(S), 0, -1):
    print(x)
for k, v in enumerate(dp):
    print(k, v)
print(ans)
