def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)#key-value : 내림차순
    print(numbers)
    return str(int(''.join(numbers)))

import functools
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return(int(t1)> int(t2)) - (int(t1)<int(t2))

def solution2(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    return str(int(''.join(n)))

a = [6,10,2]
b = solution(a)
print(b)
