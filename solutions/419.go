package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "unicode"
)

type R []rune

var (
	t    R
	W    = Print
	i    = 0
	s, _ = b.NewReader(Stdin).ReadString('\n')
)

func F(s R) bool {
	k := len(s)
	j := 0

	for j < k {
		k--
		if s[j] != s[k] {
			return 1 < 0
		}
		j++
	}

	return 1 > 0
}

func main() {
	for _, v := range s {
		if v > 64 && v < 91 || v > 96 && v < 123 {
			t = append(t, ToLower(v))
		}
	}

	n := len(t)
	n--
	for i < n && t[i] == t[n] {
		i++
		n--
	}

	z := append(append(append(R{}, t[:i]...), t[n]), t[i:]...)
	if F(z) {
		goto A
	}

	z = append(append(append(R{}, t[:n+1]...), t[i]), t[n+1:]...)
	if F(z) {
		goto A
	}

	z = t
	z[n] = z[i]
	if F(z) {
		goto A
	}

	W("NO")
	return
A:
	W(`YES
`, string(z))
}