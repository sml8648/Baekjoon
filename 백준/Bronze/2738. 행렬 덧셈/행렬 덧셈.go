package main

import (
	"fmt"
)

func main() {
	var N, M int
	fmt.Scan(&N, &M)

	// Initialize matrices A and B
	A := make([][]int, N)
	B := make([][]int, N)
	for i := 0; i < N; i++ {
		A[i] = make([]int, M)
		B[i] = make([]int, M)
	}

	// Input matrix A
	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			fmt.Scan(&A[i][j])
		}
	}

	// Input matrix B
	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			fmt.Scan(&B[i][j])
		}
	}

	// Add matrices A and B
	C := make([][]int, N)
	for i := 0; i < N; i++ {
		C[i] = make([]int, M)
		for j := 0; j < M; j++ {
			C[i][j] = A[i][j] + B[i][j]
		}
	}

	// Output the result matrix
	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			fmt.Print(C[i][j], " ")
		}
		fmt.Println()
	}
}