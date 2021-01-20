# 최고 : O((M+N)*logN), 최악 : O(M*logN)
n = int(input())
array = list(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')