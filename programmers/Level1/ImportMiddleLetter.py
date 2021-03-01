def solution(s):
    if len(s) % 2 == 1:
        return s[len(s)//2]
    else:
        return s[len(s)//2-1] + s[len(s)//2]


s = "abcde"
print(solution(s))


# def string_middle(str):
#     return str[(len(str)-1)//2:len(str)//2+1]