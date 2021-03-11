T = int(input())
nums = list(map(int, input().split()))
sosu = 0

for i in nums:
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            sosu += 1
print(sosu)

