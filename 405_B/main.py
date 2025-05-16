N, M = map(int, input().split())
A = list(map(int, input().split()))

# 存在するかしないかのハッシュテーブルを作成する
exist = {x: False for x in range(1, M + 1)}

# print(exist)

# 全部trueだったら、OKで、後ろからstackでとる
# 一つでもfalseがあったら、ダメだから、0を出力する

count = 0

while M <= len(A):
  for a in A:
    exist[a] = True
  
  if all(exist.values()):
    A.pop()
    count += 1
    exist[a] = False
  
  # elif False in exist.values():
  else:
    break
    
print(count)
  