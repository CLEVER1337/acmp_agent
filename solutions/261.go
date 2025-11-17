
package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

type Node struct {
	cnt   int32
	child [10]int32 // -1 = absent, otherwise index of the child
}

// create a node with all children set to -1
func newNode() Node {
	var n Node
	for i := 0; i < 10; i++ {
		n.child[i] = -1
	}
	return n
}

func main() {
	in := bufio.NewReader(os.Stdin)

	var N, M, K int
	if _, err := fmt.Fscan(in, &N, &M, &K); err != nil {
		return
	}

	// Δ[1..M]
	delta := make([]int64, M+2) // extra cell for safety
	var prev int64 = 0
	for i := 1; i <= M; i++ {
		var a int
		fmt.Fscan(in, &a)
		delta[i] = int64(a) - prev
		prev = int64(a)
	}

	// ---------- build trie ----------
	// root = index 0
	nodes := make([]Node, 0, N*M+2)
	nodes = append(nodes, newNode()) // root

	for i := 0; i < N; i++ {
		var s string
		fmt.Fscan(in, &s)
		if len(s) < M {
			s = strings.Repeat("0", M-len(s)) + s
		} else if len(s) > M {
			s = s[:M]
		}
		cur := 0
		for pos := 0; pos < M; pos++ {
			d := int(s[pos] - '0')
			childIdx := int(nodes[cur].child[d])
			if childIdx == -1 {
				childIdx = len(nodes)
				nodes = append(nodes, newNode())
				nodes[cur].child[d] = int32(childIdx)
			}
			cur = childIdx
			nodes[cur].cnt++
		}
	}

	// ---------- depth‑first search ----------
	ans := math.MaxInt64

	var dfs func(idx, depth int, cum int64)
	dfs = func(idx, depth int, cum int64) {
		if depth == M {
			if cum < ans {
				ans = cum
			}
			return
		}
		// is there a missing digit among 0..K-1 ?
		missing := false
		for dig := 0; dig < K; dig++ {
			if nodes[idx].child[dig] == -1 {
				missing = true
				break
			}
		}
		if missing {
			if cum < ans {
				ans = cum
			}
		}
		// go deeper
		for dig := 0; dig < K; dig++ {
			childIdx := int(nodes[idx].child[dig])
			if childIdx != -1 {
				newCum := cum + delta[depth+1]*int64(nodes[childIdx].cnt)
				dfs(childIdx, depth+1, newCum)
			}
		}
	}

	dfs(0, 0, 0)

	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, ans)
	out.Flush()
}
