# 예제 3-1 거스름돈

n = 1260
count = 0

# 큰 단위 화폐부터 차례대로 확인

coin_types = [500,100,50,10]

for coin in coin_types:
    count += (n // coin) # 몫을 더하기 
    n %= coin # 나머지 

print(count)