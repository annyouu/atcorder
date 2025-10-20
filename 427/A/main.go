package main

import (
	"fmt"
)

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func main() {
	var S, A, B, X int
	fmt.Scan(&S, &A, &B, &X)

	time := 0
	total := 0

	for time < X {
		// 移動時間
		runTime := min(A, X - time)
		total += S * runTime
		time += runTime

		if time >= X {
			break
		}

		// 休憩時間
		restTime := min(B, X - time)
		time += restTime
	}

	fmt.Println(total)
}