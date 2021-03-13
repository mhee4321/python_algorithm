from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 거리 초기화
# 자기자신 거리 0
distance = [-1] * (n+1)
distance[x] = 0

# 출발지 x 삽입
q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

result = 0

for i in range(1, n+1):
    if k == distance[i]:
        print(i)
        result += 1

if result == 0:
    print(-1)

