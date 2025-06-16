# N = int(input())
# A = list(map(int, input().split()))
# count = 0
# result = []

# # Aに、x以上の要素が重複を含めてx回以上現れる
# for i in range(len(A)+1):
#   for value in A:
#     if i <= value:
#       count += 1
#   result.append(count)
#   count = 0
    

# print(result)

###### 全探索では非効率 ######

# ソートで考える
N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True) # 大きい順に並べる

x = 0
for i in range(N):
    if A[i] >= i + 1:
        x = i + 1
    else:
        break
    
print(x)
