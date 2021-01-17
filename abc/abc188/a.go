package main

import (
	"fmt"
	"math"
)

func main() {
	var X, Y float64
	fmt.Scan(&X, &Y)
	if math.Abs(X-Y) < 3 {
		fmt.Print("Yes")
	} else {
		fmt.Print("No")
	}
}
