def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    print(len(progresses))
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0 #초기화
            time += 1
    answer.append(count)
    return answer

a = [93,30,55]
b = [1,30,5]
c = solution(a,b)
print(c)