package main

import (
	"fmt"
)

func main() {
	var h1, m1, h2, m2 int
	fmt.Scan(&h1, &m1, &h2, &m2)

	total := h1 * 60 + m1
	total1 := h2 * 60 + m2

	diff := total - total1
	if diff < 0 {
		fmt.Println("No")
	} else {
		fmt.Println("Yes")
	}
}