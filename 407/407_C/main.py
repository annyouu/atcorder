from collections import deque

S = input()

queue = deque()
visited = set()

queue.append(("", 0))

while queue:
    t, count = queue.popleft()

    if t == S:
        print(count)
        break

    if len(t) > len(S):
        continue

    visited.add(t)

    # Aボタンを押す tの末尾に0を追加する
    queue.append((t + "0", count + 1))
    # Bボタンを押す　各桁を+1(9,0)
    if t:
        next_t = ''.join(str((int(c) + 1) % 10) for c in t)
        queue.append((next_t, count + 1))

# from collections import deque

# S = input()

# queue = deque()
# visited = set()

# queue.append((S, 0))

# while queue:
#     t, count = queue.popleft()

#     if t == "":
#         print(count)
#         break

#     if t in visited:
#         continue
#     visited.add(t)

#     # 操作Aの逆：末尾0なら削除する
#     if t.endswith("0"):
#         queue.append((t[:-1], count + 1))
    
#     # 操作Bの逆： 各桁 -1
#     prev_t = ''.join(str((int(c) - 1) % 10) for c in t)
#     queue.append((prev_t, count + 1))