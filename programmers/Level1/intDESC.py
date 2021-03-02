def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    return int(''.join(n))

def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)));

n = 118372
print(solution(n))