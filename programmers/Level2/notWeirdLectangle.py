import math

# gcd = 최대공약
def solution(w,h):
    total = w * h
    total -= w+h-math.gcd(w, h)
    return total

수
w = 8
h = 12
print(solution(8, 12))