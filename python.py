
# import itertools
#
# def solve(i):
#
#     return i
#
# H, W, K = map(int, input().split())
# S = [input() for _ in range(H)]
# ans = H + W
# for i in range(2 ** (H - 1)):
#     ans = min(ans, solve(i))

# import itertools
# H, K, W = map(int, input().split())
# S = []
# for i in range(H):
#     S.append([int(s) for s in input()])
# # print(S)
#
# for t in itertools.product([0, 1], repeat=H - 1):
#     # print("t:", t, "横ライン")
#     cnt = t.count(1)
#     # print(cnt)
#     print(S[0])
#     lst = [[s for s in S[0]]]
#     print(lst)
# n = int(input())
# a = [int(n) for n in input().split()]
# lst = [0 for _ in range(2 * 100000)]
# ans = 0
# for i in a:
#     lst[i] = lst[i] + 1
# for i in lst:
#     if i != 0:
#         ans = ans + (i * (i - 1) / 2)
# for i in a:
#     x = lst[i]
#     if x != 0 or x != 1:
#         print((ans - (x * (x - 1) / 2) + ((x - 1) * (x - 2) / 2)).__int__())
# l = int(input())
# print(l * l * l / 3 / 3 / 3)
# s = input()
# n = s.__len__()
# hn = ((n - 1) / 2).__int__()
# qn = (hn / 2).__int__()
# ans = 'Yes'
# for i in range(hn):
#     if s[i] != s[n-1-i]:
#         ans = 'No'
# for i in range(qn):
#     if s[i] != s[hn-1-i]:
#         ans = 'No'
# print(ans)
# n, m = map(int, input().split())
# ans = n * (n - 1) / 2 + m * (m - 1) / 2
# print(ans.__int__())
# abm = [int(n) for n in input().split()]
#
# a = abm[0]
# b = abm[1]
# m = abm[2]
# am, bm = 1000000, 1000000
# al = [int(n) for n in input().split()]
# bl = [int(n) for n in input().split()]
# for i in al:
#     if am > i:
#         am = i
# for i in bl:
#     if bm > i:
#         bm = i
# ans = am + bm
#
# for i in range(m):
#     x, y, c = map(int, input().split())
#     x = x - 1
#     y = y - 1
#     cur = al[x] + bl[y] - c
#     if cur < ans:
#         ans = cur
#
# print(ans)

# S = input()
# ans = "Yes"
# if S.__len__() % 2 != 0:
#     ans = "No"
# else:
#     for i in range( len(S) ):
#         if i % 2 == 0 and S[i] == "h":
#             continue
#         elif i % 2 == 1 and S[i] == "i":
#             continue
#         else:
#             ans = "No"
# print(ans)
