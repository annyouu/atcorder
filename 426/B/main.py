S = list(input())

# # 文字列とその回数をカウントする辞書を作る

count_dict = {}

for word in S:
  if word in count_dict:
    count_dict[word] += 1
  else:
    count_dict[word] = 1

for key, value in count_dict.items():
  if value == 1:
    print(key)
    