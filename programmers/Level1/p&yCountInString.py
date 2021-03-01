def solution(s):
    s = s.lower()
    answer = False
    p_sum, s_sum = 0, 0
    for i in s:
        if 'p' == i:
            p_sum += 1
        elif 'y' == i:
            s_sum += 1
    if p_sum == s_sum:
        answer = True

    return answer

def solution2(s):
    return s.lower().count('p') == s.lower().count('y')

s = "Pyy"
print(solution(s))