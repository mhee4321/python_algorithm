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

def solution2(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer

from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))