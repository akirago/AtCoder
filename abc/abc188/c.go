package main

import (
	"fmt"
	"math"
)

func main() {
	var N int
	fmt.Scan(&N)
	sN := int(math.Pow(2, float64(N)))
	A := make([]int64, sN)
	for i := 0; i < sN; i++ {
		fmt.Scan(&A[i])
	}
	fmax, smax := int64(0), int64(0)
	findex, sindex := -1, -1
	for i, rating := range A {
		if i < sN/2 {
			if rating > fmax {
				fmax = rating
				findex = i
			}
		} else {
			if rating > smax {
				smax = rating
				sindex = i
			}
		}
	}
	if fmax < smax {
		fmt.Println(findex + 1)
	} else {
		fmt.Println(sindex + 1)
	}
}
