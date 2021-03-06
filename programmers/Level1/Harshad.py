def solution(x):
    answer = False
    sum = 0
    list_x = list(str(x))
    for i in list_x:
        sum += int(i)
    if x % sum == 0:
        answer = True
    return answer

def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0


arr = 10
print(solution(arr))