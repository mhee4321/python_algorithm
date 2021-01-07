def solution(prices):
    answer = [0] * len(prices) #[0,0,0,0,0]
    print(answer)
    for i in range(len(prices)-1): #0~4
        for j in range(i,len(prices)-1):
            if prices[i] > prices[j]: #감소함
                break
            else:
                answer[i] += 1
    return answer
a = [1,2,3,2,3]
print(solution(a))

