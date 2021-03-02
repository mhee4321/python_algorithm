# 시간초과
def solution(arr):
    result = []
    for num in arr:
        if num == min(arr):
            continue
        else:
            result.append(num)
    if not result:
        result.append(-1)
    return result

def solution2(arr):
    answer = []
    minVal = min(arr)
    arr.remove(minVal)
    # arr이 빈배열이라면
    if not arr:
        arr.insert(0,-1)
    return arr



arr = [4, 3, 2, 1]
print(solution(arr))