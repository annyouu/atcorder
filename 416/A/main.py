N, L, R = list(map(int, input().split()))
S = list(input())

for i in range(L-1, R):
    if S[i] == 'x':
        print('No')
        break

print("Yes")