N = int(input())

S = [input() for _ in range(N)]

results = set()

for i in S:
    for k in S:
        if i == k:
            continue
        combined = i + k
        results.add(combined)

print(len(results))