package main
import (
	. "fmt"
	. "math/big"
)
func main() {
	var a, b Int
	Scan(&a, &b)
	Print(a.Mul(&a, &b))
}