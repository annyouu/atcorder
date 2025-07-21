from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()
    S = '0' + S
    safe = [S == '0' for s in S]
    max_state = 1 << N

    visited = [False] * max_state
    visited[0] = True

    queue = deque([0])

    while queue:
        state = queue.popleft()
        for i in range(N):
            if not (state >> i) & 1:
                new_state = state | (i << i)
                if not visited[new_state] and safe[new_state]:
                    visited[new_state] = True
                    queue.append(new_state)
    
    if visited[max_state - 1]:
        print("Yes")
    else:
        print("No")
