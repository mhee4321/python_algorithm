def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if answer == []: # if not answer:
        answer.append(-1)
    answer.sort()
    return answer

1
2
def solution2(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

arr = [5, 9, 7, 10]
divisor = 5
print(solution(arr, divisor))