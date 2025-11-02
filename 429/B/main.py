# 自分の作ったコード O(N^2)

N, M = map(int, input().split())

A = list(map(int, input().split()))

count = 0
no_count = 0

for i in range(len(A)):
    B = A.copy()

    # i番目の要素を削除する
    B.pop(i)

    # Bの合計を求める
    total = 0
    for x in B:
        total += x
    
    if total == M:
        count += 1
    else:
        no_count += 1

if count > 0:
    print("Yes")
else:
    print("No")

# もっと速いコード
# n, m = map(int, input().split())
# a = list(map(int, input().split()))

# if sum(a) - m in a:
#     print("Yes")
# else:
#     print("No")