time = list(map(int, input().split()))
h = []
m = []

for i in range(len(time)):
  if i % 2 == 0:
    h.append(time[i])
  else:
    m.append(time[i])

# 時間を分単位にする
total = h[0] * 60 + m[0]
total1 = h[1] * 60 + m[1]

diff = total - total1
if diff < 0:
  print("No")
else:
  print('Yes')
    