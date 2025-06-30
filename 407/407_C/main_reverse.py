S = input().strip()
n = len(S)

# B 操作回数を計算
b = (int(S[-1]) - 0) % 10
for i in range(n-1, 0, -1):
  curr = int(S[i-1])
  nex = int(S[i])
  b += (curr - nex) % 10

# A 操作回数はn回
ans = n + b
print(ans)