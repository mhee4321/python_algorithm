def solution(seoul):
    for i, s in enumerate(seoul):
        if s == "Kim":
            return "김서방은 " + str(i) +"에 있다"


def solution2(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))


seoul =["Jane", "Kim"]
print(solution(seoul))

