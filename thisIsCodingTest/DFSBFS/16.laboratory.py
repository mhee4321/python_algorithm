n, m = map(int, input().split())
after_gate = [[0] * m for _ in range(n)]
data = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 정답(바이러스 전파 후에도 살아남은 0의 개수)
result = 0


for _ in range(n):
    data.append(list(map(int, input().split())))

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if after_gate[nx][ny] == 0:
                after_gate[nx][ny] = 2
                virus(nx, ny)

# 현재 맵 after_gate에서 안전영역 0의 개수를 구하는 메소드
def calculate():
    score = 0
    for i in range(n):
        for j in range(m):
            if after_gate[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    # gate 3개 설치하면
    if count == 3:
        for i in range(n):
            for j in range(m):
                # 게이트 설치 이후 리스트에 넣어줌
                after_gate[i][j] = data[i][j]
        # 전파 진행
        for i in range(n):
            for j in range(m):
                if after_gate[i][j] == 2:
                    virus(i, j)
        result = max(result, calculate())
        return

    # 빈 공간에 울타리 3개 무작위로 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
# 울타리 수가 0일때부턴 시작
dfs(0)
print(result)

