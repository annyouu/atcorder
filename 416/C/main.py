from itertools import product
N, K, X = list(map(int, input().split()))


S = [input() for _ in range(N)]

a = []
for indices in product(range(N), repeat=K):
  combined = ''.join(S[i] for i in indices)
  a.append(combined)

# 辞書順にソートする
a.sort()

print(a[X - 1])

