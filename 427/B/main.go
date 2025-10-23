package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)

	var N, K int
	fmt.Fscan(in, &N, &K)

	var S string
	fmt.Fscan(in, &S)

	count := make(map[string]int)

	// K文字の部分文字列をカウントする
	for i := 0; i <= N-K; i++ {
		t := S[i:i+K]
		count[t]++
	}

	// 最大値を求める
	maxCount := 0
	for _, v := range count {
		if v > maxCount {
			maxCount = v
		}
	}

	// 最大値を持つキーを収集する
	var result []string
	for k, v := range count {
		if v == maxCount {
			result = append(result, k)
		}
	}

	// 辞書順にソートする
	sort.Strings(result)

	// 出力
	fmt.Println(maxCount)
	for _, r := range result {
		fmt.Println(r)
	}
}