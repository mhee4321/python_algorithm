def solution(s):
    s = sorted(s, reverse= True)
    return ''.join(s)

s = "Zbcdefg"
print(solution(s))