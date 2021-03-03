def solution(numbers, hand):
    answer = ''
    lastL = 10 # "*"
    lastR = 12 # "#"

    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            lastL = i
        elif i in [3, 6, 9]:
            answer += "R"
            lastR = i
        else:
            i = 11 if i == 0 else i

            absL = abs(i-lastL)
            absR = abs(i-lastR)

            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                lastR = i
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                lastL = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lastL = i
                else:
                    answer += 'R'
                    lastR = i
    return answer





numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))