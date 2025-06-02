def main():

    n = int(input())
    p = list(map(int, input().split()))

    # ランレングス圧縮
    v = []
    for i in range(n - 1):
        if p[i] < p[i + 1]:
            if not v or v[-1][0] == ">":
                v.append(["<", 1])
            else:
                v[-1][1] += 1
        
        else:
            if not v or v[-1][0] == "<":
                v.append([">", 1])
            else:
                v[-1][1] += 1
    
    ans = 0
    

if __name__ == '__main__':
    main()