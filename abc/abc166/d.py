X = int(input())
A = 0
B = 0
for i in range(10 ** 2):
    for j in range(- 10 ** 2, 10 ** 2):
        if i ** 5 - j ** 5 == X:
            A = i
            B = j
print(A, B)