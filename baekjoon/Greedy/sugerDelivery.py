# n = int(input())
# answer = 0
# kilo_type = [5,3]
#
# for kilo in kilo_type:
#     if n not in list kilo_type:
#         return -1
#     answer += n//kilo
#     n%=kilo
# print(answer)

n = int(input())

answer = 0
while n>=0:
    if n%5==0:
        answer += n//5
        print(answer)
        break
    n -=3
    answer +=1
else:
    print(-1)