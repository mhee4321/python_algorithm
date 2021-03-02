def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

def solution2(a, b):
    return sum([x*y for x, y in zip(a, b)])

a = [1,2,3,4]
b = [-3,-1,0,2]
print(solution(a, b))