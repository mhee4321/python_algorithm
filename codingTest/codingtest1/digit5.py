def solution(N):
    # 음수
    if N<0:
        N = -(N)
        for i in range(0, 3):
            sol = list(map(int, str(N)))
            if sol[i] > 5:
                sol.insert(0,5)
                break
            elif sol[i+1] > 5:
                sol.insert(1,5)
                break
            elif sol[i+2] > 5:
                sol.insert(2,5)
                break
            else:
                sol.insert(3,5)
                break
        print('-', "".join(map(str, sol)))
    else:
        for i in range(0, 3):
            sol = list(map(int, str(N)))
            if sol[i] < 5:
                sol.insert(0,5)
                break
            elif sol[i+1] <5:
                sol.insert(1,5)
                break
            elif sol[i+2] < 5:
                sol.insert(2,5)
                break
            else:
                sol.insert(3,5)
        print("".join(map(str, sol)))





a = int(input())
solution(a)