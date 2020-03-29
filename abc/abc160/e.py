X, Y, A, B, C = map(int, input().split())
p = [int(n) for n in input().split()]
q = [int(n) for n in input().split()]
r = [int(n) for n in input().split()]
p.sort(reverse=True)
q.sort(reverse=True)
px = p[0: X]
qx = q[0: Y]
t = px + qx + r
t.sort(reverse=True)
print(sum(t[0: X + Y]))