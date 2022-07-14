# 동전 개수 구하기 문제


n, k = map(int, input().split())

coin =[int(input()) for _ in range(n)]

count = 0

for i in reversed(range(n)):
    count += k//coin[i]
    k = k%coin[i]
        
print(count)