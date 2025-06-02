H, W, N = list(map(int, input().split()))

a = []
b = []

for _ in range(N):
  ai, bi = map(int, input().split())
  a.append(ai)
  b.append(bi)

Q = int(input())

# query = [input().split() for _ in range(Q)]
# query = [(int(t), int(v)) for t, v in query]
query = [tuple(map(int, input().split())) for _ in range(Q)]

row = [[] for _ in range(H + 1)]
col = [[] for _ in range(W + 1)]

for i in range(N):
  row[a[i]].append(i)
  col[b[i]].append(i)

# ゴミがすでに捨てられたか
used = [False] * N
# 行、列のクエリがすでに使われたか
row_done = [False] * (H + 1)
col_done = [False] * (W + 1)

# クエリ処理
for t, v in query:
  if t == 1:
    if row_done[v]:
      print(0)
    else:
      cnt = 0
      for idx in row[v]:
        if not used[idx]:
          used[idx] = True
          cnt += 1
      
      row_done[v] = True
      print(cnt)
  else:
    if col_done[v]:
      print(0)
    else:
      cnt = 0
      for idx in col[v]:
        if not used[idx]:
          used[idx] = True
          cnt += 1
      col_done[v] = True
      print(cnt)