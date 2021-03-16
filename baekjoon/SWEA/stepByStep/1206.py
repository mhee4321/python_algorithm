for test_case in range(1, 11):
    T = int(input())
    bds = list(map(int, input().split()))
    result = 0
    for i in range(2, T - 2):
        if bds[i] > bds[i-2] and bds[i] > bds[i-1] and bds[i] > bds[i+1] and bds[i] > bds[i+2]:
            result += bds[i] - max(bds[i-2], bds[i-1], bds[i+1], bds[i+2])
    print(f'#{test_case} {result}')