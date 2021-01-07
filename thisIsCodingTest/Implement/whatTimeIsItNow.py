n = int(input())

count = 0
for i in range(n+1): #항상 i~n까지 i<=x<range(), 0,1,2,3
    for j in range(60): #0,1,2,3~59
        for k in range(60): #0,1,2,3~59
            if '3' in str(i) +str(j) + str(k):
                count +=1
print(count)
