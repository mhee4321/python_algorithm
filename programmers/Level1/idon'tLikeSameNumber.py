def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

def solution2(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer

arr = [1,1,3,3,0,1,1]
print(solution2(arr))