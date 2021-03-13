# isalpha(), isdigit() 사용, isalnum() -> 알파벳 또는 숫자인지 확인
# ''.join 사용시 모든 문자열 str 형태여야 함

n = input()

sum = 0
answer_list = []

for i in n:
    if i.isalpha():
        answer_list.append(i)
    else:
        sum += int(i)
answer_list.sort()

if sum != 0:
    answer_list.append(str(sum))

print(''.join(answer_list))
