import sys
from collections import Counter

def input():
    return int(sys.stdin.readline())

def print(v):
    sys.stdout.write(str(v) + '\n')


n = input()
data = sorted([input() for _ in range(n)])

print(round(sum(data) / n))  # 평균
print(data[n // 2])  # 중앙값
# 최빈값
count = Counter(data).most_common()
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

print(data[-1] - data[0])  # 범위