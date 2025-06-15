# from collections import deque
# N, Q = map(int, input().split())
# A = deque()
# # 最初の整数列A(キューにする)

# for i in range(1, N+1):
#   A.append(i)

# for _ in range(Q):
#   query = list(map(int, input().split()))
  
#   # タイプ１の処理
#   if query[0] == 1:
#     idx = query[1] - 1 # Aのindexに合わせる
#     item = query[2]
#     A[idx] = item
    
#   # タイプ２の処理
#   elif query[0] == 2:
#     idx = query[1] - 1
#     print(A[idx])
  
#   # タイプ３の処理
#   # Aの先頭の要素を末尾にする操作をk回
#   else:
#     K = query[1]
#     A.rotate(-K)
#     for _ in range(K):
#       A.append(A.popleft())
#       # キューのpopleftで先頭から取り出して
#       # appendで末尾に追加

############ 計算量を減らす工夫 #########

N, Q = map(int, input().split())
A = [i + 1 for i in range(N)]
offset = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p = query[1] - 1
        x = query[2]
        A[(p + offset) % N] = x
    elif query[0] == 2:
        p = query[1] - 1
        print(A[(p + offset) % N])
    else:
        k = query[1]
        offset = (offset + k) % N



    
    
