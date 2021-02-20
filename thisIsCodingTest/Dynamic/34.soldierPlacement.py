# https://www.acmicpc.net/problem/18353

# LIS(Longest Increasing Subsequence) 최장길이 부분수열
# D[i] = max(D[i], D[j] + 1) if array[j] < array[i]

n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
