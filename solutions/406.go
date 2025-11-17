
package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

type Exp struct {
	letter byte
	prob   float64
}
type Obs struct {
	letter byte
	prob   float64
}

func main() {
	in := bufio.NewReader(os.Stdin)

	var N, M int
	if _, err := fmt.Fscan(in, &N, &M); err != nil {
		return
	}

	// original order and its probabilities
	origOrder := make([]byte, N)
	origProb := make([]float64, N)
	for i := 0; i < N; i++ {
		var s string
		var p float64
		fmt.Fscan(in, &s, &p)
		origOrder[i] = s[0]
		origProb[i] = p
	}

	var ciphertext string
	fmt.Fscan(in, &ciphertext)

	// frequencies of each cipher letter
	cnt := make([]int, 26)
	for _, ch := range ciphertext {
		cnt[int(ch-'a')]++
	}

	// observed frequencies (including zero for letters that do not appear)
	observed := make([]Obs, 26)
	for i := 0; i < 26; i++ {
		prob := float64(cnt[i]) / float64(M)
		observed[i] = Obs{letter: byte('a' + i), prob: prob}
	}

	// expected probabilities (only N letters)
	expected := make([]Exp, N)
	for i := 0; i < N; i++ {
		expected[i] = Exp{letter: origOrder[i], prob: origProb[i]}
	}

	// sort both lists by probability, ties by letter for determinism
	sort.Slice(observed, func(i, j int) bool {
		if observed[i].prob < observed[j].prob {
			return true
		}
		if observed[i].prob > observed[j].prob {
			return false
		}
		return observed[i].letter < observed[j].letter
	})
	sort.Slice(expected, func(i, j int) bool {
		if expected[i].prob < expected[j].prob {
			return true
		}
		if expected[i].prob > expected[j].prob {
			return false
		}
		return expected[i].letter < expected[j].letter
	})

	const K = 26
	const INF = 1e100
	dp := make([][]float64, N+1)
	for i := 0; i <= N; i++ {
		dp[i] = make([]float64, K+1)
		for j := 0; j <= K; j++ {
			dp[i][j] = INF
		}
	}
	for j := 0; j <= K; j++ {
		dp[0][j] = 0
	}

	for i := 1; i <= N; i++ {
		for j := 1; j <= K; j++ {
			// skip observed[j-1]
			dp[i][j] = dp[i][j-1]
			// match observed[j-1] with expected[i-1]
			cost := math.Abs(expected[i-1].prob - observed[j-1].prob)
			cand := dp[i-1][j-1] + cost
			if cand < dp[i][j] {
				dp[i][j] = cand
			}
		}
	}

	// reconstruct mapping
	mapping := make(map[byte]byte) // original -> cipher
	i, j := N, K
	const eps = 1e-12

	for i > 0 {
		if j == 0 { // should never happen for a correct DP
			break
		}
		costMatch := dp[i-1][j-1] + math.Abs(expected[i-1].prob-observed[j-1].prob)
		if math.Abs(dp[i][j]-costMatch) < eps {
			// we used this match
			mapping[expected[i-1].letter] = observed[j-1].letter
			i--
			j--
		} else {
			// skip observed[j-1]
			j--
		}
	}

	// output in the order of the input letters
	out := bufio.NewWriter(os.Stdout)
	for i := 0; i < N; i++ {
		fmt.Fprintln(out, string(mapping[origOrder[i]]))
	}
	out.Flush()
}
