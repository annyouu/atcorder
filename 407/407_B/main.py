X, Y = map(int, input().split())

all_count = 36

satisfy_count = 0

for i in range(1, 7):
    for j in range(1, 7):
        if i + j >= X or abs(i - j) >= Y:
            satisfy_count += 1

ans = satisfy_count / all_count
print(ans)