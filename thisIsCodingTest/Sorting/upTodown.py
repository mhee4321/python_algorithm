n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

# 내림차순
array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')