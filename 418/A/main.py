# 末尾がteaかを判定する問題
N = int(input())
S = input()

if N < 3:
    print("No")
else:
    # if S[-3] == 't' and S[-2] == 'e' and S[-1] == 'a':
    #     print("Yes")
    # else:
    #     print("No")
    if S[-3:] == "tea":
        print("Yes")
    else:
        print("No")