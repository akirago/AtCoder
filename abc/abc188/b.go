package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	A, B := make([]float64, N), make([]float64, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&A[i])
	}
	for i := 0; i < N; i++ {
		fmt.Scan(&B[i])
	}

	total := float64(0)
	for i := 0; i < N; i++ {
		total += A[i] * B[i]
	}
	if total == 0 {
		fmt.Print("Yes")
	} else {
		fmt.Print("No")
	}
}
