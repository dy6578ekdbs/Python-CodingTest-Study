# +로 최대한 수를 크게 만든 후, 
# -가 나올 때 뺀다.


# - 기준으로 자른다. 
arr = input().split('-') 
s = 0


# 만약에 원소 하나면..? 
for i in arr[0].split('+'):
    s += int(i)

# 첫번 째 원소부터, 끝까지(default), 한칸 간격으로(default)
for i in arr[1:]:
    for j in i.split('+'):
      
        s -= int(j)


print(s)

