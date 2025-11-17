
package main

import (
	"bufio"
	"fmt"
	"os"
	"math/big"
)

func main() {
	in := bufio.NewReader(os.Stdin)

	var N int
	var R string
	if _, err := fmt.Fscan(in, &N); err != nil {
		return
	}
	fmt.Fscan(in, &R)

	L := len(R)
	if L == 0 {
		fmt.Println(0)
		return
	}
	if N > L { // more original letters than output letters -> impossible
		fmt.Println(0)
		return
	}

	// ----- mapping letters -> (key index, position on key) -----
	keyStrings := []string{
		"ABC", // 0 -> key 2
		"DEF", // 1 -> key 3
		"GHI", // 2 -> key 4
		"JKL", // 3 -> key 5
		"MNO", // 4 -> key 6
		"PQRS",// 5 -> key 7 (4 letters)
		"TUV", // 6 -> key 8
		"WXYZ",// 7 -> key 9 (4 letters)
	}
	maxPress := []int{3, 3, 3, 3, 3, 4, 3, 4}

	keyOf := make(map[byte]int) // letter -> key index 0..7
	posOf := make(map[byte]int) // letter -> position 1..3/4
	for ki, s := range keyStrings {
		for i, ch := range s {
			keyOf[byte(ch)] = ki
			posOf[byte(ch)] = i + 1 // positions are 1‑based
		}
	}

	// ----- arrays for the received string -----
	keyIdx := make([]int, L)   // key index for each character
	posArr := make([]int, L)   // position for each character
	for i := 0; i < L; i++ {
		c := R[i]
		keyIdx[i] = keyOf[c]
		posArr[i] = posOf[c]
	}

	// ----- DP table -----
	// dp[i][g] – number of ways to split prefix of length i into g groups
	dp := make([][]*big.Int, L+1)
	for i := 0; i <= L; i++ {
		dp[i] = make([]*big.Int, N+1)
		for g := 0; g <= N; g++ {
			dp[i][g] = new(big.Int)
		}
	}
	zero := big.NewInt(0)
	one := big.NewInt(1)
	dp[0][0].Set(one)

	// ----- main DP -----
	for i := 0; i < L; i++ {
		key := keyIdx[i]
		maxP := maxPress[key]
		for g := 0; g < N; g++ {
			if dp[i][g].Cmp(zero) == 0 {
				continue
			}
			sum := 0
			// try all possible end positions j
			for j := i; j < L && keyIdx[j] == key; j++ {
				sum += posArr[j]
				if sum > maxP {
					break // longer j would only increase the sum
				}
				// add the new group (i..j)
				dp[j+1][g+1].Add(dp[j+1][g+1], dp[i][g])
			}
		}
	}

	ans := dp[L][N]
	// if ans is zero, String() prints "0"
	fmt.Println(ans.String())
}
