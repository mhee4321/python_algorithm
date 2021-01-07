import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

def solution2(participant, completion):
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

a = ['mislav', 'stanko', 'mislav', 'ana']
b = ['stanko', 'ana', 'mislav']
print(solution2(a,b))

