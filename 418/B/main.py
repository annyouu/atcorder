# S = input()

# ans = []
# count = 0

# # 充足率の計算

# for i in range(len(S)):
#   # 初めのtのindexをstartに代入する
#   if S[i] == "t":
#     start = i
#     break
#   else:
#     start = 0

# # endは最後からfor文を回してtを見つけたらそのindexを代入する
# for i in range(len(S) -1, -1,-1):
#   if S[i] == "t":
#     end = i + 1
#     break
#   else:
#     end = 0

# if start == 0 and end == 0:
#   print(0)
# else:
#   # スライスで文字列を抽出する
#   A = S[start:end]
  
#   # tの数を数える
#   count_t = 0
#   for s in A:
#     if s == "t":
#       count_t += 1
  
#   # 充足率の計算
#   count = (count_t - 2) / (len(A) - 2)
#   print(count)

S = input()
N = len(S)
f = 0

for i in range(N):
    for j in range(i+1, N+1): # S[i:j]の部分文字列
        t = S[i:j]
        if len(t) < 3:
            continue
        if t[0] != "t" or t[-1] != "t":
            continue
        count_t = t.count('t')
        rate = (count_t - 2) / (len(t) - 2)
        f = max(f, rate)

print(f)
