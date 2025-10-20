from collections import defaultdict

N, K = map(int, input().split())
S = input()

count = defaultdict(int)

# K文字の部分文字列を取得する
for i in range(N - K + 1):
  t = S[i:i+K]
  count[t] += 1

# 最大値を求める
max_count = max(count.values())

# 最大のものを辞書順に並べる

result = sorted([key for key, val in count.items() if val == max_count])

print(max_count)
for r in result:
  print(r)