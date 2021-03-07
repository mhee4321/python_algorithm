import math

def solution(w,h):
    total = w * h
    total -= w+h-math.gcd(w, h)
    return total


w = 8
h = 12
print(solution(8, 12))