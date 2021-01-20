# 전형적인 이진탐색 문제
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    sum = 0
    # 몫
    mid = (start+end) // 2
    for x in array:
        if x > mid:
            sum += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽록 부분 탐색)
    if sum < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 기
        result = mid
        start = mid + 1

print(result)
