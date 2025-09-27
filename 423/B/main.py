N = int(input())
L = list(input().split())

left_count = 1
right_count = 1

# 左側
for word in L:
    if word == '1':
        break
    left_count += 1

# 右側
for word in reversed(L):
    if word == '1':
        break
    right_count += 1

total_rooms = N + 1

ans = total_rooms - (left_count + right_count)

if ans < 0:
    ans = 0

print(ans)