package main

import "fmt"

func countBinarySequences(N int) int {
    if N == 1 {
        return 1
    }
    if N == 2 {
        return 2
    }

    dp := make([]int, N+1)
    dp[1], dp[2] = 1, 2

    for i := 3; i <= N; i++ {
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    }

    return dp[N]
}

func main() {
    var N int
    fmt.Scanln(&N)

    result := countBinarySequences(N)
    fmt.Println(result)
}
