
package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

// countMaxDepthAtMost returns the number of correct bracket sequences
// of semilength n whose depth never exceeds k.
// It works for any k (including negative) – for k < 0 the answer is 0.
func countMaxDepthAtMost(n, k int) *big.Int {
	if k < 0 {
		return big.NewInt(0)
	}
	if k > n { // depth cannot be larger than n anyway
		k = n
	}
	// cur[h] – number of prefixes with current balance h
	cur := make([]big.Int, k+1)
	cur[0].SetInt64(1) // empty prefix
	nxt := make([]big.Int, k+1)

	steps := 2 * n
	for i := 0; i < steps; i++ {
		// reset nxt
		for j := 0; j <= k; j++ {
			nxt[j].SetInt64(0)
		}
		// transition
		for h := 0; h <= k; h++ {
			if cur[h].Sign() == 0 {
				continue
			}
			if h+1 <= k {
				nxt[h+1].Add(&nxt[h+1], &cur[h]) // add '('
			}
			if h > 0 {
				nxt[h-1].Add(&nxt[h-1], &cur[h]) // add ')'
			}
		}
		cur, nxt = nxt, cur
	}
	// answer is the number of full sequences, i.e. balance 0 at the end
	res := new(big.Int)
	res.Set(&cur[0])
	return res
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var N, K int
	if _, err := fmt.Fscan(in, &N, &K); err != nil {
		return
	}

	// sequences with depth <= K
	atMostK := countMaxDepthAtMost(N, K)
	// sequences with depth <= K-1 (zero for K==0)
	atMostKminus := countMaxDepthAtMost(N, K-1)

	// exact depth = atMostK - atMostKminus
	ans := new(big.Int)
	ans.Sub(atMostK, atMostKminus)

	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, ans.String())
	out.Flush()
}
