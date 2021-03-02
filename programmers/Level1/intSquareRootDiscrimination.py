def solution(n):
    for i in range(1, 10000000):
        if i**2 == n:
            return (i+1)**2
    return -1

def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1

n = 3
print(solution(n))
