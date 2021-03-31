# Hanoi's Top
# F(N) = 2 * F(N-1) + 1
def hanoi(st, ed, num):
    if num == 1:
        print(st, ed)
        return
    hanoi(st, 6 - ed - st, num-1) # 1단계
    print(st, ed) # 2단계
    hanoi(6 - ed - st, ed, num-1) # 3단계

N = int(input())
print(2**N-1)
hanoi(1, 3, N)




