answer = 0
def dfs(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx == N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    dfs(idx+1, numbers, target, value+numbers[idx])
    dfs(idx+1, numbers, target, value-numbers[idx])

def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))