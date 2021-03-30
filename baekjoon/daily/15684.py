# i, j, k에 사다리 설치
def check(i, j, k):
    pass

# result
def result():
    pass

answer = 4
N = int()
# 반복문으로 모든 경우 탐색
for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            p = check(i, j, k)
            if p and result(): answer = min(answer, p)
print(answer)

