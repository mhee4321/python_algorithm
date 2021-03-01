def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]

    strings.sort()

    for j in range(len(strings)):
        answer.append(strings[j][1:])
    return answer

def solution2(strings, n):
    return sorted(strings, key=lambda x: x[n])

strings = ["sun", "bed", "car"]
n = 1
print(solution(strings, n))