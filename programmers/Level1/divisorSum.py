def solution(n):
    answer = []
    for i in range(1, n+1):
        for j in range(n, i-1, -1):
            if i * j == n:
                answer.append(i)
                answer.append(j)
    return sum(set(answer))

def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

def sumDivisor(num):
    return sum(filter(lambda x: num % x == 0, range(1, num + 1)))

n = 5
print(solution(n))
