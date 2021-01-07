n = 5555
count = 0
coin_types = [500, 100, 50, 10] #내림차순
for coin in coin_types:
    count += n//coin #몫
    n%=coin #나머지
print(count)