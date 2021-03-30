def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:
        return lst[0] * 5000 + 50000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]:
            return 10000 + lst[1] * 1000
        return 2000 + (lst[1] + lst[2]) * 500
    for i in range(3):
        if lst[i] == lst[i+1]: return 1000 + lst[i] * 100
    return lst[-1] * 100

# N = int(input())
# print(max(money() for i in range(N)))


def mine(n):
    lst = []
    for _ in range(n):
        lst.append(sorted(list(map(int, input().split()))))
    print(lst)
    for i in range(n):
        if len(set(lst[i])) == 1:
            return lst[i][0] * 5000 + 50000
        if len(set(lst)) == 2:
            if lst[i][1] == lst[i][2]:
                return 10000 + lst[i][1] * 1000
            return 2000 + (lst[i][1] + lst[i][2]) * 500
        for j in range(3):
            if lst[i][j] == lst[i][j+1]:
                return 1000 + lst[i][j] * 100
        return lst[i][-1] * 100


n = int(input())
print(mine(n))