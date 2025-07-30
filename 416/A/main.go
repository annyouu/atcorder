package main

import (
	"fmt"
)

func main() {
	var N, L, R int
	fmt.Scan(&N, &L, &R)

	var S string
	fmt.Scan(&S)

	for i := L - 1; i < R; i++ {
		if S[i] == 'x' {
			fmt.Println("No")
			return
		}
	}
	fmt.Println("Yes")
}