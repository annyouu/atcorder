# deque
from collections import deque

# q = deque()

# # 末尾に追加
# q.append(1)

# # 先頭に追加
# q.appendleft(2)

# # 末尾から取り出す
# print(q.pop())

# # 先頭から取り出す
# print(q.popleft())

q = deque()
Q = input()

for _ in range(Q):
    s = input().split()
    if s[0] == "1":
        x = s[1]
        q.append(x)
    elif s[0] == "2":
        print(q.popleft())
