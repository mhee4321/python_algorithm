def solution(bridge_length, weight, truck_weights):

    time = 0
    q = [0]*bridge_length

    while q:
        time += 1
        q.pop(0)  # 다리를 건너는 트럭
        if truck_weights: #대기 트럭
            if sum(q)+truck_weights[0] <=weight:
                q.append(truck_weights.pop(0)) #q의 맨뒤에 붙임
            else:
                q.append(0) #q의 맨뒤에 아무것도 안붙임(0)
                # print(q.append(0))

    return time

a = 2
b = 10
c = [7,4,5,6]
d = solution(a,b,c)
print(d)