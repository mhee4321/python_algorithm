T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    div, mod = divmod(N, H)
    if mod == 0:
        print('{}{:02d}'.format(H, div))
    else:
        print('{}{:02d}'.format(mod, div+1))