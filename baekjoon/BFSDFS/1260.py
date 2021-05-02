def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visit[v] = 0
    while(queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0] # queue.pop()하면 맨 뒤에께 빠짐(리스트형태)
        for i in range(1, n+1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0



n, m, v = map(int, input().split())
s = [[0] * (n+1) for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    s[a][b] = 1
    s[b][a] = 1

dfs(v)
print()
bfs(v)