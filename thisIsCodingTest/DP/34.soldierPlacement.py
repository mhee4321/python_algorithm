n = int(input())
data = list(map(int, input().split()))
solution = 0

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if data[i] < data[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(solution)

