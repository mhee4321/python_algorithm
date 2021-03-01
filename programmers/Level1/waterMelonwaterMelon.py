def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer

def solution2(n): return ('수박'*n) [:n]

n = 3
print(solution(n))