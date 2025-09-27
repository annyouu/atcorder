S = list(input())

S_first = int(S[0])
S_last = int(S[2])

# ステージが最後だった時
if S_last == 8:
  S_first += 1
  S_last = 1
else:
  # 通常時
  S_last += 1
  
S_result = str(S_first) + S[1] + str(S_last)
  
print(S_result)