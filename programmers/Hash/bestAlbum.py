def solution(genres, plays):
    answer = [] #배열array, 들어가는 원소의 종류가 다양할 때
    dic1 = {} #dictionary {"mouse" : 3, "penguin" :5} () : tuple 들어가는 원소의 종류가 동일할 때
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
