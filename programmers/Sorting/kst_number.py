def solution(array, commands): #실패작
    answer = []
    for i in commands:
        a = array[commands[i][0]-1:commands[i][1]]
        a.sort()
        answer += a[commands[i][2]-1]
    return answer

def solution2(array, commands):
    answer = []
    # commands에 있는 command(i, j, k)를 뽑는다.
    for command in commands: #[2,5,3] [4,4,1] [1,7,3]
        i, j, k = command[0], command[1], command[2] #2,5,3
        slice = array[i - 1:j]  # array에서 슬라이스를 하고
        slice.sort()  # 정렬하고
        answer.append(slice[k - 1])  # 인덱싱하자
    return answer

def solution3(array, commands):
    answer = []
    for i, j, k in commands:
        slice = array[i-1:j]
        slice.sort()
        answer.append(slice[k-1])
    return answer

a = [1,5,2,6,3,7,4]
b = [[2,5,3],[4,4,1],[1,7,3]]
c = solution2(a,b)
print(c)