
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type Fenwick struct {
	n   int
	bit []int
}

func NewFenwick(n int) *Fenwick {
	return &Fenwick{
		n:   n,
		bit: make([]int, n+2), // 1‑based
	}
}

// Add delta at position idx
func (f *Fenwick) Add(idx, delta int) {
	for idx <= f.n {
		f.bit[idx] += delta
		idx += idx & -idx
	}
}

// Sum of elements on prefix [1..idx]
func (f *Fenwick) Sum(idx int) int {
	sum := 0
	for idx > 0 {
		sum += f.bit[idx]
		idx -= idx & -idx
	}
	return sum
}

func main() {
	in := bufio.NewReader(os.Stdin)

	var N, M, P int
	if _, err := fmt.Fscan(in, &N, &M, &P); err != nil {
		// no input
		return
	}

	// Read all performances
	type perf struct {
		a, e int
	}
	arr := make([]perf, P)
	for i := 0; i < P; i++ {
		var a, e int
		fmt.Fscan(in, &a, &e)
		arr[i] = perf{a: a, e: e}
	}

	// Sort by athlete number (rating) ascending.
	// Performances with equal rating must not be counted against each other.
	sort.Slice(arr, func(i, j int) bool {
		if arr[i].a != arr[j].a {
			return arr[i].a < arr[j].a
		}
		// tie‑breaker not important, but keep stable order
		return arr[i].e < arr[j].e
	})

	bit := NewFenwick(M)
	var totalPrev int = 0 // total number of processed performances (with smaller a)
	var answer int64 = 0

	i := 0
	for i < P {
		// Find block with the same athlete number
		end := i
		for end < P && arr[end].a == arr[i].a {
			end++
		}

		// Query contributions of this block against all previous blocks
		for k := i; k < end; k++ {
			e := arr[k].e
			// number of previous performances with exercise > e
			inv := int64(totalPrev - bit.Sum(e))
			answer += inv
		}

		// After queries, add this block into the BIT
		for k := i; k < end; k++ {
			bit.Add(arr[k].e, 1)
			totalPrev++
		}

		i = end
	}

	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, answer)
	out.Flush()
}
