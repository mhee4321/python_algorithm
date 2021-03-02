def solution(s, n):
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for char in s:
        if char in low:
            ist = low.find(char) + n
            answer += low[ist % 26]
        elif char in up:
            ist = up.find(char) + n
            answer += up[ist % 26]
        else:
            answer += " "
    return answer

def solution2(s, n):
    s = list(s)
    for i in range(len(s)):
        # 대문자이면
        if s[i].isupper():
            # ord = 문자의 아스키 코드 값을 돌려주는 함수
            # chr = 아스키 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

s = "a B z"
n = 4
print(solution2(s, n))
