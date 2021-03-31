def checkBrankets(list):
    answer = False
    stack = []
    for i in list:
        if i == '(' or i == '[':
            stack.append(i)
        else:
            if not stack:
                return answer
            elif i == ')':
                if stack[-1] == '(':
                    stack = stack[:-1]
                else:
                    stack.append(i)
            else:
                if stack[-1] == '[':
                    stack = stack[:-1]
                else:
                    stack.append(i)
    if not stack:
        answer = True
    return answer


def judge(list):
    stack = []
    for i in list:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                tmp = 0
                for j in range(len(stack) - 1, -1, -1):
                    if stack[j] == '(':
                        stack[-1] = tmp * 2
                        break
                    else:
                        tmp += stack[j]
                        stack = stack[:-1]
        elif i == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                tmp = 0
                for j in range(len(stack) - 1, -1, -1):
                    if stack[j] == '[':
                        stack[-1] = tmp * 3
                        break
                    else:
                        tmp += stack[j]
                        stack = stack[:-1]
    return sum(stack)


n = input()
if checkBrankets(n) == False:
    print(0)
else:
    print(judge(n))