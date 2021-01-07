from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1)))) # 모든 경우의 수를 만듬
    a -= set(range(0, 2)) # 숫자 0과 1은 제거

    # 모든 경우의 수에 대해서 소수 판정
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

a = "17"
b = "011"