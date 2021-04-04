def era(a, b):
    cnt = 0
    nums = [True] * (a+1)
    for i in range(2, len(nums) + 1):
        for j in range(i, a+1, i):
            if nums[j] == True:
                nums[j] = False
                cnt = cnt + 1
                if cnt == b:
                    print(j)
                    break

def mine(a, b):
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
