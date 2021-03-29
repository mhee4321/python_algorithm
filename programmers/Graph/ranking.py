from collections import defaultdict

def solution(n, results):
    answer = 0
    wins = defaultdict(set) # 값이 없으면 {key : set()}으로 저장됨
    loses = defaultdict(set)

    # wins
    # {4: {2, 3, 5}, 3: {2, 5}, 1: {2, 5}, 2: {5}, 5: set()}
    # loses
    # {3: {4}, 2: {1, 3, 4}, 5: {1, 2, 3, 4}, 1: set(), 4: set()}
    for a, b in results:
        wins[a].add(b)
        loses[b].add(a)

    for i in range(1, n + 1):
        for loser in wins[i]:
            loses[loser] |= loses[i]
        for winner in loses[i]:
            wins[winner] |= wins[i]

    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
