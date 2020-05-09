N, A, B, C = map(int, input().split())
ans = []
d = {'A': A, 'B': B, 'C': C}
s = [input() for _ in range(N)]


def add_ans(s1, s2):
    d[s1] += 1
    d[s2] -= 1
    ans.append(s1)


for i in range(N):
    now = s[i]
    x = now[0]
    y = now[1]
    if d[x] == d[y] == 0:
        print('No')
        exit()
    elif d[x] == 0:
        add_ans(x, y)
    elif d[y] == 0:
        add_ans(y, x)
    elif i == N - 1:
        add_ans(x, y)
    elif x in s[i + 1]:
        add_ans(x, y)
    else:
        add_ans(y, x)

print("Yes")
for i in ans:
    print(i)
