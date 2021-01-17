# 삽입정렬 O(n^2)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    # range(start, end, step) :  start -> end+1까지 1씩 감소
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            continue
print(array)
