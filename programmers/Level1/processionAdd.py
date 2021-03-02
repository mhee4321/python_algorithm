def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1


import numpy as np
def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()

def sumMatrix(A,B):
    answer = []
    for i, j in zip(A, B):
        temp =[]
        for t1, t2 in zip(i,j):
            temp.append(t1+t2)
        answer.append(temp)

    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution(arr1, arr2))
