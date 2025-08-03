package main

import (
	"fmt"
)

func main() {
	var N, A, B int
	fmt.Scan(&N, &A, &B)

	var S string
	fmt.Scan(&S)

	// スライスで抽出
	result := S[A : N-B]
	fmt.Println(result)
}