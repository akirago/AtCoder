# X = int(input())  # N
# Y = int(input())  # M
# way = [input() for _ in range(Y)]
X = 3  # N
Y = 4  # M
way = ["#S#.", "....", ".#.G"]
INF = 1000000
dp = [[INF for _ in range(Y)] for _ in range(X)]
print(dp)
calc = []
goal = (0, 0)
for x in range(X):
    for y in range(Y):
        if way[x][y] == "S":
            calc.append((x, y))
            dp[x][y] = 0
        if way[x][y] == "G":
            goal = (x, y)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

while calc.__sizeof__():
    xy = calc.pop()
    if xy == goal:
        break
    for i in range(4):
        nx = xy[0] + dx[i]
        ny = xy[1] + dy[i]
        print(nx, ny)
        if 0 <= nx < X and 0 <= ny < Y and dp[nx][ny] == INF and way[nx][ny] != "#":
            calc.append((nx, ny))
            dp[nx][ny] = dp[xy[0]][xy[1]] + 1

print(dp[goal[0]][goal[1]])
