S, A, B, X = list(map(int, input().split()))


time = 0
total = 0

while time < X:
  # 移動時間
  run_time = min(A, X - time)
  total += S * run_time
  time += run_time
    
  if time >= X:
      break
    
  # 休憩時間
  rest_time = min(B, X - time)
  time += rest_time

print(total)