def solution(clothes):
    clothes_type = {} #dictionary
    cnt = 1

    for _, t in clothes:
        print(_)
        print(t)
        if t not in clothes_type:
            clothes_type[t] = 2 #새로운 옷을 입거나 안입거나
        else:
            clothes_type[t] += 1 #옷의 종류만 하나 추가됨

    for num in clothes_type.values():
        cnt *= num

    return cnt-1

c = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(c))