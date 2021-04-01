# BFS
# 숨바꼭질 = 내위치, 동생의 위치
from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

def bfs(n):
    de=deque()
    de.append(n)
    ch[n][0]=0
    ch[n][1]=1

    while de:
        x=de.popleft()

        for i in (x+1, x-1, x*2):
            if 0 <= i < 100001:
                if ch[i][0] == -1: # 처음 방문하는 경우
                    ch[i][0] = ch[x][0]+1
                    ch[i][1] = ch[x][1]
                    de.append(i)

                elif ch[i][0] == ch[x][0]+1: # 한번 이상 방문한 경우
                    ch[i][1] += ch[x][1] # 방법 더하기

n, k = map(int, input().split())
ch = [[-1, 0] for i in range(1000001)]

bfs(n)
print(ch[k][0])
print(ch[k][1])