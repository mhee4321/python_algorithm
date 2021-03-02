def solution(s):
    if s.count('-') > 0:
        return int(s)
    else:
        return int(s)


def solution2(s):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            # 4*(10^0) + 3(10^1) + 2(10^2) + 1(10^3)
            result += int(number) * (10 ** idx)
    return result

s = "-1234"
print(solution(s))