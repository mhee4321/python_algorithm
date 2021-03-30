def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
        
def gcdEuclid(a,b):
    return b if a%b==0 else gcd(b, a%b)

def lcm(a, b):
    return a*b // gcd(a,b)
