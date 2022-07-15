# 5
# 3 1 4 3 2


n = int(input())
time = list(map(int, input().split()))
time.sort()


delay = 0

for i in range(n): 
    for j in range(i+1):
        delay += time[j]


print(delay)
