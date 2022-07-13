from click import secho

n, m = map(int, input().split()) 

result = 0

for i in range(n):
    data = list(map(int, input().split())) # 이번 행 숫자들 
    min_value = min(data) # 이번 행에서 가장 작은 수 찾기
    result = max(result, min_value) # 더 큰 수 찾기 


# for i in range(n):
   # data = list(map(int, input().split())) # 이번 행 숫자들 
   # min_value = 10001
   # for a in data:
   #     min_value = max(result, a) # 더 큰 수 찾기 
   # result = max(result,min_value)

print(result)