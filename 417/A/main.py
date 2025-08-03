N,A,B = list(map(int, input().split()))

S = input()

R = []
# startからendの配列を持ってくる
start = A
end = N - B

for i in range(start, end):
    R.append(S[i])

print(*R, sep='')
