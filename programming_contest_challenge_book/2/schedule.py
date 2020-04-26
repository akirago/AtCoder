n = 5
s = [int(n) for n in "1 2 4 6 8".split()]
t = [int(n) for n in "3 5 7 9 10".split()]
st = []
for i in range(n):
    st.append((t[i], s[i]))

ans = 0
now = 0
while st.__len__():
    now = min(st)[0]
    st = list(filter(lambda x: now <= x[1], st))
    ans += 1
print(ans)
