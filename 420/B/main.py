N, M = map(int, input().split())
s = [input().strip() for _ in range(N)]

pt = [0] * N

for j in range(M):
    x = 0
    y = 0

    for i in range(N):
        if s[i][j] == '0':
            x += 1
        else:
            y += 1
    
    # 得点の計算
    for i in range(N):
        if s[i][j] == '0':
            if x <= y:
                pt[i] += 1
        
        else:
            if x >= y:
                pt[i] += 1

high = max(pt)

ans = []
for i in range(N):
    if pt[i] == high:
        ans.append(str(i + 1))

print(" ".join(ans))