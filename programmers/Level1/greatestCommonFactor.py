def solution(n, m):
    for i in range(1, n+1):
        if n % i == 0:
            if m % i == 0:
                gcd = i
    if gcd == 1:
        lcm = n*m
    else:
        lcm = gcd * (n // gcd) * (m // gcd)
    return [gcd, lcm]

def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

n = 2
m= 5
print(solution(n, m))

