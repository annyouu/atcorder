package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)

	var Q int
	fmt.Fscan(in, &Q)

	A := []int{0}
	B := []int{0}

	for i := 0; i < Q; i++ {
		var queryType string
		fmt.Fscan(in, &queryType)

		if queryType == "1" {
			var c string
			fmt.Fscan(in, &c)

			prevA := A[len(A) - 1]
			var nextA int

			if c == "(" {
				nextA = prevA + 1
			} else {
				nextA = prevA - 1
			}

			A = append(A, nextA)

			prevB := B[len(B) - 1]
			var nextB int

			if nextA < prevB {
				nextB = nextA
			} else {
				nextB = prevB
			}

			B = append(B, nextB)
		} else if queryType == "2" {
			if len(A) > 1 {
				A = A[:len(A) - 1]
				B = B[:len(B) - 1]
			}
		}

		// 判定
		if A[len(A)-1] == 0 && B[len(B)-1] == 0 {
			fmt.Println("Yes")
		} else {
			fmt.Println("No")
		}
	}
}
