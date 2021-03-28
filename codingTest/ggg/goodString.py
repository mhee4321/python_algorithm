# 백준 13432
# 조함
from itertools import combinations
def solution(s):
    count = 0
    s_list = list(s)

    # 개수가 하나일때
    case1 = []
    for i in s_list:
        if i not in case1:
            case1.append(i)
            count += 1
    # 개수가 두개이상일 때
    for z in range(2, count+1):
        p_list = list(map(''.join, combinations(s_list, z)))
        for i in p_list:
            case2 = []
            for j in i:
                if len(case2) == 0:
                    case2.append(j)
                if j not in case2:
                    case2.append(j)
                    count += 1

    return count // 2


s = "abcd"
print(solution(s))