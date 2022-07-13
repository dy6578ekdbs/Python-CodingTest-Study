# 단순하게 푼 나의 답안

n, m = map(int, input().split())

count = 0

while True:
    if n == 1:
        break

    if (n % m) == 0:
        n //= m
        count += 1
    else :
        n -= 1
        count += 1

print(count)

### n 값이 클 때의 답안 ###

n, k = map(int, input().split())
result = 0

# n이 k 이상이라면, k로 나눈다. 
while n >= k:
    # 나누어 떨어지지 않는다면, -1을 반복 
    while n % k != 0:
        n -= 1
        result += 1
    # n을 k로 나누기
    n //= k
    result += 1 

# 남은 값에 대해서 1씩 빼기
while n > 1 :
    n -= 1
    result += 1

print(result)