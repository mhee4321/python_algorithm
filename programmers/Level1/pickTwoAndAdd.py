from itertools import combinations

def solution(numbers):
    answer = set()
    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))
    return sorted(answer)



a = [2,1,3,4,1]
print(solution(a))

# def solution(numbers):
#     answer = list()
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] + numbers[j] not in answer:
#                 answer.append(numbers[i] + numbers[j])
#     answer.sort()
#     return answer


# from itertools import combinations
# def solution(numbers):
#     return sorted(list(set([sum([i,j]) for i,j in combinations(numbers,2)])))