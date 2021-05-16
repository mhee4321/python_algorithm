from itertools import permutations
def solution2(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1)))) # 모든 경우의 수를 만듬
    a -= set(range(0, 2)) # 숫자 0과 1은 제거

    # 모든 경우의 수에 대해서 소수 판정
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


##
import itertools

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True

def solution(numbers):
    num = [d for d in numbers]
    print(num)
    per_total = []
    for i in range(1,len(num)+1):
        per = list(map(int, list(map(''.join, list(itertools.permutations(num, i))))))
        per_total.extend(list(set(per)))# iterable의 모든 항목을 넣기
    per_total = list(set(per_total))
    tmp = []
    for n in per_total:
        tmp.append(is_prime(n))
    return sum(tmp)

a = "17"
b = "011"
print(solution(a))