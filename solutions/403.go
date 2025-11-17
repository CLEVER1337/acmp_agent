
package main

import "fmt"

// ---------- pre‑computed powers of 3 ----------
var pow3 [10]int

func init() {
	pow3[0] = 1
	for i := 1; i < 10; i++ {
		pow3[i] = pow3[i-1] * 3
	}
}

// ---------- decimal digits, most significant first ----------
func digitsOf(n int64) []int {
	if n == 0 {
		return []int{0}
	}
	var d []int
	for n > 0 {
		d = append(d, int(n%10))
		n /= 10
	}
	// reverse
	for i, j := 0, len(d)-1; i < j; i, j = i+1, j-1 {
		d[i], d[j] = d[j], d[i]
	}
	return d
}

// ---------- count of valid numbers in [1 .. N] ----------
func countValid(N int64) int64 {
	if N < 0 {
		return 0
	}
	digits := digitsOf(N)
	n := len(digits)

	// dp[pos][started][mask] – only for tight == false
	dp := make([][2]map[int]int64, n+1)
	for i := 0; i <= n; i++ {
		dp[i][0] = make(map[int]int64) // started == false
		dp[i][1] = make(map[int]int64) // started == true
	}

	var dfs func(pos int, started bool, mask int, tight bool) int64
	dfs = func(pos int, started bool, mask int, tight bool) int64 {
		if pos == n {
			if started {
				return 1
			}
			return 0
		}
		if !tight {
			mp := dp[pos][0]
			if started {
				mp = dp[pos][1]
			}
			if v, ok := mp[mask]; ok {
				return v
			}
		}
		limit := 9
		if tight {
			limit = int(digits[pos])
		}
		var total int64 = 0
		for d := 0; d <= limit; d++ {
			newTight := tight && d == limit
			newStarted := started || d != 0
			if !newStarted {
				// still only leading zeros – mask stays 0
				total += dfs(pos+1, false, 0, newTight)
			} else {
				cnt := (mask / pow3[d]) % 3
				if cnt >= 2 {
					continue // would use digit d three times
				}
				newMask := mask + pow3[d]
				total += dfs(pos+1, true, newMask, newTight)
			}
		}
		if !tight {
			mp := dp[pos][0]
			if started {
				mp = dp[pos][1]
			}
			mp[mask] = total
		}
		return total
	}

	return dfs(0, false, 0, true)
}

// ---------- main ----------
func main() {
	var L, R int64
	if _, err := fmt.Scan(&L, &R); err != nil {
		return
	}
	ans := countValid(R) - countValid(L-1)
	fmt.Println(ans)
}
