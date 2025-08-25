package main

import (
	"fmt"
)



func main() {
	var X, Y int
	fmt.Scan(&X, &Y)

	A := X + Y

	if A > 12 {
		totalA := A - 12
		fmt.Println(totalA)
	} else {
		fmt.Println(A)
	}
}
