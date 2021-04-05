# table[y][x] = table[y-1][x] + table[y][x-money[y]]
# table[y][x] = 0부터 y까지의 화폐로 i원을 내는 법
def solution(n, money):
    table = [[0 for _ in range(n+1)] for _ in range(len(money))]
    table[0][0] = 1
    # 동전의 최솟값으로 만들 수 있는 값들, 최소 동전이 1이 아닌 경우도 있을 수 있으므로
    for i in range(money[0], n+1, money[0]):
        table[0][i] = 1
    for y in range(1, len(money)):
        for x in range(n+1):
            if x >= money[y]:
                table[y][x] = (table[y-1][x] + table[y][x - money[y]]) % 100000007
            else:
                table[y][x] = table[y-1][x]
    return table[-1][-1]

n = 5
money = [1, 2, 5]
print(solution(n, money))