package main

import "fmt"

func main1() {
	var N, M int
    fmt.Scan(&N, &M)

    // 配列の作成
    A := make([]int, N)
    for i := 0; i < N; i++ {
        fmt.Scan(&A[i])
    }

    count := 0
    no_count := 0

    for i := 0; i < len(A); i++ {
        B := make([]int, len(A))
        copy(B, A)

        // i番目を削除する
        B = append(B[:i], B[i+1:]...)

        // 合計を求める
        total := 0
        for _, x := range B {
            total += x
        }

        if total == M {
            count++
        } else {
            no_count++
        }
    }

    if count > 0 {
        fmt.Println("Yes")
    } else {
        fmt.Println("No")
    }
}
