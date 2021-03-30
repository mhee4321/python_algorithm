a = input()
b = input()

while not a==b:
    if a>b: a//=2
    else: b//=2
print(a)