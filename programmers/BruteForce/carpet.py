def solution(brown, red):
    for index in range(1,red+1): #1,2
        if red%index == 0:
            length = red//index
            if (((index+2)*(length+2))-(index*length)) == brown:
                return [max(index+2,length+2),min(index+2,length+2)]

def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]

print(solution(10,2))