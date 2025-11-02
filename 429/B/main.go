package main

import "fmt"

func sum(arr []int) int {
    total := 0
    for _, v := range arr {
        total += v
    }
    return total
}

func main() {
    var N, M int
    fmt.Scan(&N, &M)

    A := make([]int, N)
    for i := 0; i < N; i++ {
        fmt.Scan(&A[i])
    }

    // 合計を出す
    result := sum(A)

    for _, v := range A {
        if result - M == v {
            fmt.Println("Yes")
            return
        }
    }
    fmt.Println("No")
}