# def circle_area(radius):
#     return 3.14 * radius * radius

# area = circle_area(5)
# print(area)

# for i in range(2,10):
#     for j in range(1,10):
        # print(i*j, end=" ")
    # print('')

# for i in range(len(marks)):
#     if marks[i] < 60:
#         continue
    # print("%d번 학생 합격!" % (i+1))

# def add_many(*args): # 무슨 변수가 들어올지 모를 때 사용
#     result = 0
#     for i in args:
#         result = result + i
#     return result
#
# print(add_many(1,2,3,4,5))
#
# add = lambda a, b: a+b
# result = add(3,4)
# print(result)

a = [[10, 20], [30, 40], [50, 60]]
for i in a:
    for j in i:
        print(j, end=' ')
    print()

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

for i in a:
    print('%s %d' %(i,len(i))) # [10, 20] 2

