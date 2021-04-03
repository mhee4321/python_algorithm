def era(a, b):
    count = 0
    ck= [False for _ in range(a+1)]
    for i in range(2, a+1):
        if ck[i] == True:
            continue
        ck[i] = True
        count += 1
        if count == b:
            return i
        for j in range(i*i, a+1, i):
            ck[j] = True
            count += 1
            if count == b:
                return j

a, b = map(int, input().split())
print(era(a, b))
