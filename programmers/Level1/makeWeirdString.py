def solution(s):
    s = list(s)
    answer = []
    for idx, str in enumerate(s):
        if idx % 2 == 0:
            answer.append(str.upper())
        else:
            answer.append(str.lower())
    return ''.join(answer)

def solution2(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))


def toWeirdCase(s):
    answer = []
    for x in s.split(' '):
        str1 = ''
        for i, y in enumerate(x):
            if i % 2 == 0:
                str1 += y.upper()
            else:
                str1+= y.lower()
        answer.append(str1)

    return ' '.join(answer)

s = "try hello world"
print(toWeirdCase(s))