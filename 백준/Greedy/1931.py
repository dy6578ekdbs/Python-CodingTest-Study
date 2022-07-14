# 가장 빨리 끝나는 회의 순으로 정렬 필요 !!! (끝나는 시간의 오름차순)
# 끝나는 시간이 같은 경우 : 시작 하는 순서대로 정렬 되어있어야한다. (시작하는 시간의 오름차순)
# 예를 들어 아래와 같은 경우, 
# 2
# 2 2
# 1 2
# 의 경우 이 상태로 한다면 (2 2)가 되고 (1 2)는 (2 2)의 끝나는 시간보다 시작시간이 일찍이기 때문에 무시되어 1번의 회의가 진행된다고 나온다. 하지만 정렬을 통해 (1 2)가 먼저 선택되면 (2 2)도 선택이 가능해지기 때문에 가능한 회의는 2번으로 결정된다.


## 구글링 참고해서 짠 코드 
n = int(input()) 
time = [ list(map(int,input().split()))  for _ in range(n)]

time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

last = 0 # 회의의 마지막 시간을 저장할 변수
count = 0 # 회의 개수를 저장할 변수

for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    count += 1
    last = j

print(count)





#### 처음 풀었던 코드 (시간초과) ####
from operator import itemgetter

count = 1

n = int(input()) # 회의 개수 

# 회의 시간 
m = [ list(map(int,input().split()))  for _ in range(n)]

m.sort(key=itemgetter(1), reverse=False)

end = m[0][1] 

for i in range(n-1):
    if m[i+1][0] >= end:
        print("성공 : ", i)
        count += 1
        end = m[i+1][1]

print(count)