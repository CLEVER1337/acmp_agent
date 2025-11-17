
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)

	var N, M int64
	if _, err := fmt.Fscan(in, &N, &M); err != nil {
		return
	}

	// total number of street segments (each segment is walked at least once)
	base := 2*N*M + N + M

	// number of adjacent pairs we can create on each side (pairs of odd‑degree vertices)
	floorM := (M - 1) / 2 // pairs on bottom + top
	floorN := (N - 1) / 2 // pairs on left  + right

	var cross int64
	if M%2 == 0 && N%2 == 0 { // both even
		cross = N + M
	} else if M%2 == 0 && N%2 == 1 { // M even, N odd
		cross = N
	} else if M%2 == 1 && N%2 == 0 { // M odd, N even
		cross = M
	} else { // both odd
		cross = 0
	}

	// extra length needed to make all vertex degrees even
	extra := 2*floorM + 2*floorN + cross

	answer := base + extra

	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, answer)
	out.Flush()
}
