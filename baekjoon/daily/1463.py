# n = int(input())
# dp = [0 for _ in range(n + 1)]
#
# for i in range(2, n + 1):
#     dp[i] = dp[i - 1] + 1
#     if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
#         dp[i] = dp[i // 2] + 1
#     if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
#         dp[i] = dp[i // 3] + 1
#
# print(dp[n])

a = int(input())
count = 0
minimum = [a]


def cal(a):
    list = []
    for i in a:
        list.append(i - 1)
        if i % 3 == 0:
            list.append(i // 3)
        if i % 2 == 0:
            list.append(i // 2)
    return list


while True:
    if a == 1:
        print(count)
        break
    temp = minimum[:]
    minimum = []
    minimum = cal(temp)
    count += 1
    if min(minimum) == 1:
        print(count)
        break



