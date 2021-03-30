# O(NlogN)
def solution1(n):
    ret = 0
    for i in range(1, n+1):
        ret += len(str(i))
    return ret

def solution2(n):
    return sum(map(lambda x: len(str(x)), range(1, n+1)))


# log(10)N
def num_len(n):
    ret = 0
    while n:
         n /= 10
         ret += 1
    return ret

def solution3(n):
    l, ret = len(str(n)), 0
    for i in range(1, l):
        ret += i*(10**i - 10**(i-1))
    ret += l*(n-10**(l-1)+1)
    return ret

def mine(n):
    l = len(str(n))
    ret = 0
    for i in range(1, l):
        ret += (10-i)