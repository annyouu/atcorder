N, M, K = map(int, input().split())

H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort()
B.sort()

if all(h <= b for h, b in zip(H[:K], B[-K:])):
  print("Yes")
else:
  print("No")


