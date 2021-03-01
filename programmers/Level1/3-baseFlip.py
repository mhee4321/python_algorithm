def solution(n):

    three = ''

    # 3진법 변환
    while n>2 :
        # 몫, 나머지
        n, m = divmod(n,3)
        three += str(m)

    three += str(n)

    # 10진법으로 변환
    return int(three,3)

a = 45
# 0, 0, 2, 1
print(solution(a))