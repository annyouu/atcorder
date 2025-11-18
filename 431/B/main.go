package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)

	var X, N int
	fmt.Fscan(in, &X)
	fmt.Fscan(in, &N)

	// 重さリスト
	W := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Fscan(in, &W[i])
	}

	var Q int
	fmt.Fscan(in, &Q)

	on := make([]bool, N)

	for i := 0; i < Q; i++ {
		var pi int
		fmt.Fscan(in, &pi)
		idx := pi - 1

		if on[idx] {
			X -= W[idx]
			on[idx] = false
		} else {
			X += W[idx]
			on[idx] = true
		}

		fmt.Println(X)
	}
}