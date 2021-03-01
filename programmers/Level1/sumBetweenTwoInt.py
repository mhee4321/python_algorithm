def solution(a, b):
    answer = 0
    if a == b:
        return a
    elif a > b:
        while a != b:
            answer += a
            a -= 1
        answer += b
    elif a < b:
        while a != b:
            answer += b
            b -= 1
        answer += a
    return answer

def solution2(a, b):
    if a > b: a, b = b, a
    return sum(range(a, b+1))

a = 5
b = 3
print(solution(a, b))