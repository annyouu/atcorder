package main

import (
	"fmt"
)

func main() {
	var N, K int
	fmt.Scan(&N)

	A := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&A[i])
	}

	fmt.Scan(&K)

	count := 0
	for i := 0; i < N; i++ {
		if K <= A[i] {
			count++
		}
	}

	fmt.Println(count)
}