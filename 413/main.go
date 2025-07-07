package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var N int
	fmt.Scan(&N)

	S := make([]string, N)
	scanner := bufio.NewScanner(os.Stdin)
	for i := 0; i < N; i++ {
		scanner.Scan()
		S[i] = scanner.Text()
	}

	// 結果格納
	results := make(map[string]struct{})

	// 組み合わせ処理
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if i == j {
				continue
			}
			combined := S[i] + S[j]
			results[combined] = struct{}{}
		}
	}
	fmt.Println(len(results))
}