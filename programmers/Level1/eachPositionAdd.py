def solution(n):
    n = list(str(n))
    sum = 0
    for i in n:
        sum += int(i)
    return sum


def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10)

n = 987
print(solution(n))