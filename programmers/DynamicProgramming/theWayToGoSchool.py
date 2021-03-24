def solution(m, n, puddles):
    answer = 0
    d = [[0]*(m+1) for _ in range(n+1)]
    d[1][0] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j,i] in puddles:
                d[i][j] = 0
            else:
                # 왼쪽 + 위쪽
                d[i][j] = (d[i-1][j]+d[i][j-1])%1000000007

    return d[n][m]

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))