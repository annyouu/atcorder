X = int(input())
N = int(input())
W = list(map(int, input().split()))

Q = int(input())
P = [int(input()) for _ in range(Q)]

# hash_table = {}

# for x in P:
#   if x in hash_table:
#     hash_table[x] = True
#   else:
#     hash_table[x] = False

# # Falseの時なら、足し算を行う
# # Trueの時なら、引き算を行う

# for i in range(Q):
#   idx = P[i]
#   if hash_table[idx]:
#     X -= W[idx]
#   else:
#     X += W[idx]

# print(X)

on = [False] * N

for pi in P:
    idx = pi - 1
    if on[idx]:
        X -= W[idx]
        on[idx] = False
    
    else:
        X += W[idx]
        on[idx] = True
    
    print(X)
  