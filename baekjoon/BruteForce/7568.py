n = int(input())
s_list = []

for _ in range(n):
    weight, height = map(int, input().split())
    s_list.append((weight, height))

for i in s_list:
    rank = 1
    for j in s_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')