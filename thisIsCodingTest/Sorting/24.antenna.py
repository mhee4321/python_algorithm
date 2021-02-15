n = int(input())
data = list(map(int, input().split()))

data.sort()

print(data[0]+data[n-1] //2)

# print(data[(n-1)//2])