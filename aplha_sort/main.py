lines = ['a','c','f','d','c','d','f']

# カウント用の辞書を作る
aplha = ['a', 'b', 'c', 'd', 'f']
counter = {ch: 0 for ch in aplha}

# 文字をカウント
for val in lines:
    if val in counter:
        counter[val] += 1

# 結果を出力
for ch in aplha:
    print(f'{ch}:{counter[ch]}')