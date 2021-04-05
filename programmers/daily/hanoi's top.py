def solution(n):
    def hanoi(n, From, To, Sub):
        if n == 1:
            answer.append([From, To])
            return
        hanoi(n - 1, From, Sub, To)
        answer.append([From, To])
        hanoi(n - 1, Sub, To, From)

    answer = []
    hanoi(n, 1, 3, 2)
    return answer


def solution(n):
    def hanoi(st, ed, num):
        if num == 1:
            answer.append([st, ed])
            return
        hanoi(st, 6 - ed - st, num-1) # 1단계
        answer.append([st, ed])
        hanoi(6 - ed - st, ed, num-1) # 3단계

    answer = []
    hanoi(1, 3, n)
    return answer