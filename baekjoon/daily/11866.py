# 요세푸스 순열
from collections import deque

n, k = map(int, input().split())

dq = deque(range(1, n+1))
ans = list()

while len(dq):
    dq.rotate(-k+1)
    ans.append(dq.popleft())

print(f"<{str(ans)[1:-1]}>")