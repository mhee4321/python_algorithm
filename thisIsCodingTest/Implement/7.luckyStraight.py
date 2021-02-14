# str은 길이 len 함수를 쓸 수 있지만, int는 길이가 없어 len 함수를 쓸 수 없다.
# int만 덧셈을 할 수 있다.
n = input()

left_sum = 0
right_sum = 0

for i in range(0, len(n) // 2):
    left_sum += int(n[i])
for j in range(len(n) // 2, len(n)):
    right_sum += int(n[j])

if right_sum == left_sum:
    print('LUCKY')
else:
    print('READY')
