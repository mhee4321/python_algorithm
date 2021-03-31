# 괄호문제 = stack
def checkBranket(brankets):
    stack = []
    answer = "NO"
    for i in brankets:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return print(answer)
            else:
                stack.pop()
    if not stack:
        answer = "YES"
        return print(answer)
    else:
        return print(answer)

T = int(input())
for _ in range(T):
    branckets = input()
    checkBranket(branckets)
