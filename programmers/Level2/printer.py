from collections import deque

def solution(priorities, location):
    answer = 0
    for i in range(len(priorities)-1):
        for j in range(i+1, len(priorities)):
            if priorities[i] < priorities[j]:
                priorities.append(priorities[i])
                priorities.pop(i)
            else:
                answer += 1
                if i == location:
                    return answer



def solution2(priorities, location):
    answer = 0

    d = deque([(i, v) for i, v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[1] > item[1]:
            d.append(item)
        else:
            answer += 1
            if item[0] == location:
                break
    return answer

def solution3(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution3(priorities, location))


