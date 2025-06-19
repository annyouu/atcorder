N, L = map(int, input().split())
d = list(map(int, input().split()))

if L % 3 != 0:
  print(0)
  exit()

d = list(map(int, input().split()))
x = 0
cnt = [0] * L
for i in range(N):
  if i != 0:
    x += d[i - 1]
  x %= L
  cnt[x] += 1

ans = 0
for i in range(L // 3):
  ans +=  cnt[i] * cnt[i + L // 3] * cnt[i + 2 * L // 3]

print(ans)
