n = int(input())
data = list(map(int, input().split()))
data.sort()

answer = 1
for x in data:
    if answer < x:
        break
    answer += x

print(answer)

# 1 1 2 3 9


