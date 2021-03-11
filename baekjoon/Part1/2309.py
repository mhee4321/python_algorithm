list = []

for _ in range(9):
    list.append(int(input()))

# sum = sum(list)
# for i in range(8):
#     for j in range(i+1, 9):
#         if sum - (list[i] + list[j]) == 100:
#             one = list[i]
#             two = list[j]
#
# list.remove(one)
# list.remove(two)
# list.sort()
# for i in list:
#     print(i)

list.sort()
sum = sum(list)
for i in range(9):
    for j in range(i+1, 9):
        if sum-list[i]-list[j]==100:
            for k in range(9):
                if k==i or k == j:
                    continue
                else:
                    print(list[k])
            exit()



