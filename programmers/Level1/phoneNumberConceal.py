def solution(phone_number):
    answer = ''
    phone_number = list(phone_number)
    for i in range(0,len(phone_number)-4):
        answer += '*'
    for idx, str in enumerate(phone_number):
        if idx > len(phone_number)-5 and idx < len(phone_number):
            answer += str
    return answer

def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

def hide_numbers(s):
    if(len(s) < 5):
        return s
    else:
        return '*' + hide_numbers(s[1:])

a = "027778888"
print(solution(a))