# 케빈칙 베이컨의 6단계 법칙
import sys

INF = sys.maxsize
n, m = map(int, input().split())
a = [[INF]*n for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    a[x-1][y-1] = 1
    a[y-1][x-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                a[i][j] = 0
            else:
                a[i][j] = min(a[i][j], a[i][k] + a[k][j])

ans = []
for i in a:
    ans.append(sum(i))
for i in range(n):
    if ans[i] == min(ans):
        print(i+1)
        break
