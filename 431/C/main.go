package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func readInt(scanner *bufio.Scanner) int {
	scanner.Scan()
	val, err := strconv.Atoi(scanner.Text())
	if err != nil {
		panic(err)
	}
	return val
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	// N, M, Kを読み込む
	N := readInt(scanner)
	M := readInt(scanner)
	K := readInt(scanner)

	// H リスト (サイズ N)
	H := make([]int, N)
	for i := 0; i < N; i++ {
		H[i] = readInt(scanner)
	}

	// B リスト (サイズ M)
	B := make([]int, M)
	for i := 0; i < M; i++ {
		B[i] = readInt(scanner)
	}

	sort.Ints(H)

	sort.Ints(B)

	ison := true

	for i := 0; i < K; i++ {
		if H[i] > B[M-K+i] {
			ison = false
			break
		}
	}

	if ison {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
