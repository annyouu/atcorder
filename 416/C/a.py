from itertools import product
N = 3
K = 2

for p in product(range(N), repeat=K):
    print(p)

# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# (2, 0)
# (2, 1)
# (2, 2)
