n,m,k = map(int, input().split()) #n,m,k를 공백으로 구분하여 입력받기
data = list(map(int, input().split())) #n개의 수를 공백으로 구분하여 입력받기

data.sort(reverse=True) #내림차순 정렬
first = data[0] #가장 큰 수
second = data[1] #두번째로 큰 수

result = 0

while True:
    for i in range(k): #가장 큰 수를 k번 더하기
        if m == 0: #m이 0이면 반복문 탈출
            break
        result += first
        m -=1
    if m==0:
        break
    result +=second
    m-=1

# count = int(m/(k+1))*k
# count += m%(k+1)
#
# result +=(count)* first
# result +=(m-count)*second


print(result)

