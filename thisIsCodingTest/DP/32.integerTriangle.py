n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))


for i in range(1, n):
    for j in range(i+1):
        if j==0:
            top_left = 0
        else:
            top_left = dp[i-1][j-1]
        if j==i:
            top = 0
        else:
            top = dp[i-1][j]

        dp[i][j] = dp[i][j] + max(top, top_left)

print(max(dp[n-1]))
