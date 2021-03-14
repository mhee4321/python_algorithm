from collections import deque

n, m = map(int, input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append([graph[i][j], 0, i, j])

data.sort()
print(data)
q = deque(data)

target_time, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, time, x, y = q.popleft()
    if time == target_time:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx and nx<n and 0<=ny and ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append([virus, time+1, nx, ny])

print(graph[target_x-1][target_y-1])

