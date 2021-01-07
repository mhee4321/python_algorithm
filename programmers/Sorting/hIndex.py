def solution(citations):
    # [22, 42] , 2인 경우
    if min(citations) >= len(citations): answer = len(citations)
    else: answer = 0
    citations = sorted(citations)

    # [0] * 10000000 인 경우
    for i in range(min(citations), max(citations) + 1):
        left = 0
        right = 0
        for j in citations:
            if j <= i: left += 1
            if j >= i: right += 1
        if (left <= i) & (right >= i):
            answer = max(answer, i)
    return answer

def solution2(citations):
    citations = sorted(citations) #오름차순 0,1,3,5,6
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0




a = [3,0,6,1,5]
print(solution2(a))


