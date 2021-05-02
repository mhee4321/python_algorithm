# 웜 바이러스(DFS)
global result
result = 0

def dfs(v):
    global result
    result += 1
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)


n = int(input())
m = int(input())
s = [[0] * (n+1) for _ in range(n+1)]
visit = [0] * (n+1)


for _ in range(m):
    a, b = map(int, input().split())
    s[a][b] = 1
    s[b][a] = 1

dfs(1)
print(result-1)
