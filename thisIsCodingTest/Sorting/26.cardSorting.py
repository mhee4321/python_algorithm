# 우선순위 큐 사용 = heapq
import heapq

n = int(input())

heap_list = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap_list, data)

result = 0

while len(heap_list) != 1:
    first = heapq.heappop(heap_list)
    second = heapq.heappop(heap_list)
    sum_value = first + second
    result += sum_value
    heapq.heappush(heap_list, sum_value)

print(result)
