from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)
ans = 0

for j in range(N):
    key = j - A[j]

    ans += count[key]

    # jを使ってiを表現する
    # for一回だけで2つの役割をこなさせるように
    count[j + A[j]] += 1

print(ans)