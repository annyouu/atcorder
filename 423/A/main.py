X, C = map(int, input().split())

maxY = (1000 * X) // (1000 + C)
ans = (maxY // 1000) * 1000

print(ans)