# 백준 11687
def solution2(n):
    cache = [-1] * (n + 1)

    def count(n, div):
        if n % div != 0:
            return 0
        elif cache[n] != -1:
            return cache[n]
        else:
            return count(n // div, div) + 1

    answer = 0
    for i in range(1, n + 1):
        cache[i] = count(i, 5)
        answer += cache[i]

    return answer

def solution(n):
    if n == 0 or n == 1:
        return  0
    else:
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        fact_list = list(str(fact))

        fact_list_len = len(fact_list)

        count = 0

        for i in range(len(fact_list)):
            if fact_list[fact_list_len-1-i] !='0':
                break
            elif fact_list[fact_list_len-1-i] == '0':
                count = count + 1
        return count




n = 5
print(solution(n))