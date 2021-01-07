n,m = map(int, input().split()) #몇행 몇열

result = 0

for i in range(n): #한줄에서
    data = list(map(int, input().split())) #int로 자른 것을 list로 정리함
    min_value = min(data)
    result = max(result, min_value)

print(result)