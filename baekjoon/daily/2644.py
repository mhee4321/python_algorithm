# 촌수계산의 핵심 = 공통된 조상찾기
# 공통조상으로부터 나와 그사람의 거리 = LCA
# n<=100이기 때문에 아무리많아도 O(n^2)
n = int(input())
a, b = map(int, input().split())
p = [0 for _ in range(n+1)]

for _ in range(int(input())):
    x, y = map(int, input())
    p[y] = x

aa, ba = [], [] # a의 조상, b의 조상
ad, bd = 0, 0 # 촌수

while p[a] > 0:
    aa.append((a, ad))
    ad += 1
    a = p[a]

while p[b] > 0:
    ba.append((b, bd))
    bd += 1
    b = p[b]

for i in aa:
    for j in ba:
        if i[0] == j[0]:
            print(i[1] + j[1])
            exit()
print(-1)