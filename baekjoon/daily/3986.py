# stack
def judge(list):
    stack = []
    answer = 0
    for i in list:
        if not stack:
            stack.append(i)
            continue
        if i == 'A':
            if stack[-1] == 'A':
                stack.pop()
                continue
            else:
                stack.append(i)
        else:
            if stack[-1] == 'B':
                stack.pop()
                continue
            else:
                stack.append(i)
    if len(stack) == 0:
        answer += 1
    return answer

sum = 0
T = int(input())
for _ in range(T):
    list = input()
    sum += judge(list)
print(sum)