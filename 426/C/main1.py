N, Q = map(int, input().split())

pc = [0] + [1] * N
o = 1

for _ in range(Q):
    X, Y = map(int, input().split())
    res = 0
    while o <= X:
        res += pc[o]
        pc[Y] += pc[o]
        o += 1
    
    print(res)