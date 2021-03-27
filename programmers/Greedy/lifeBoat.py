# pop, del, remove를 사용해 리스트에서 아예 빼버리면 효율성 부분에서 틀린다.
def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people)-1
    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))