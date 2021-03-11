a, b = map(int, input().split())
sum = 0
list = []
for i in range(1, 1000):
    list += [i] * i

for i in range(a-1, b):
    sum += list[i]
print(sum)

# print(sum(list[a-1:b)))