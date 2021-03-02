def solution(n):
    n = list(str(n))
    # n.sort(reverse=True)하면 내림차순 정렬이 되어버림
    n.reverse()
    return list(map(int, n))

def digit_reverse(n):
    return list(map(int, reversed(str(n))))

n = 12345
print(solution(n))