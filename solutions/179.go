package main
import (
	. "fmt"
	. "math/big"
)
func main() {
	var k, b Int
	N := NewInt
	Scan(&k)
	Print(b.Add(b.Exp(N(3), &k, nil), N(1)))
}