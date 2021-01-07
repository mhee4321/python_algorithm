def solution(priorities, location):
    count = 0
    while(len(priorities)!=0):
        if location==0: #출력 여부를 확인하는 맨 앞순서로 왔을 경우
            if priorities[0]<max(priorities): #뒤에 중요도가 더 큰 문서가 있으면
                priorities.append(priorities.pop(0))
                location=len(priorities)-1
            else:
                return count+1 #return값 출력
        else:
            if priorities[0]<max(priorities):
                priorities.append(priorities.pop(0))
                location-=1
            else:
                priorities.pop(0)
                location-=1
                count+=1

a = [2,1,3,2]
b = 2
c = solution(a,b)
print(c)
