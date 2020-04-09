k = [1, 3, 5, 8, 11]
k.sort()


def binary_search(x):
    first = 0
    last = k.__len__() - 1
    while last - first + 1 > 0:
        c = ((last + first) / 2).__int__()
        if x == k[c]:
            return True
        elif x > k[c]:
            first = c + 1
        else:
            last = c - 1
    return False


print(binary_search(5))
