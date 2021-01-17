# 파이썬 정렬 라이브러리 O(NlogN)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array) # 오름차순
print(result)

array.sort()
print(array)

array2 = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array2, key=setting)
print(result)

