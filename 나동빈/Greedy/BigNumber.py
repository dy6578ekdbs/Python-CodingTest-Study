# 3-2 큰 수의 법칙

# N M K 
# 5 8 3

# N개의 자연수 
# 2 4 5 4 6

# K는 항상 M보다 작거나 같다

# N, M, K를 공백으로 구분해 입력받기
from unittest import result


n, m, k = map(int, input().split()) 
# N개의 수를 공백으로 구분하여 입력받기 
data = list(map(int, input().split()))

data.sort() # 정렬

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m-=1
    if m == 0 :
        break
    result += second
    m -= 1

print(result)