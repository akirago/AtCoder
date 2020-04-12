X = int(input())  # N
Y = int(input())  # M
way = [input() for _ in range(Y)]
dp = [[1000000 for _ in range(X)] for _ in range(Y)]
calc = []
for x in range(X):
    for y in range(Y):
        if way[x][y] == "S":
            calc = {x,y}

while