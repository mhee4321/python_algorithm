def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        slice = array[i-1:j]
        slice.sort()
        result.append(slice[k-1])
    return result

# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))

