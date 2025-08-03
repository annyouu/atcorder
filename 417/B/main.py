N, M = map(int, input().split())

A = list(input().split())
B = list(input().split())

for j in range(M):
    if B[j] in A:
        A.remove(B[j])

print(*A)