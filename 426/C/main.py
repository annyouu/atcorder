# 全探索(時間超過)

N, Q = map(int, input().split())

pc = [i for i in range(1, N + 1)]

for _ in range(Q):
    X, Y = map(int, input().split())
    count = 0
    for i in range(N):
        if pc[i] <= X:
            pc[i] = Y
            count += 1
    
    print(count)