

def solution(S, C):
    cost = 0
    array = list(S)


    for i in range(0, len(S)-1):
        if array[i] == array[i+1]:
            cost += min(C[i], C[i+1])
            # if C[i] < C[i+1]:
            #     array.pop(i)
            # else:
            #     array.pop(i+1)
    print(cost)


n = input()
m = list(map(int, input().split(',')))

solution(n, m)
