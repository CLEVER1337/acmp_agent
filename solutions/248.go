
package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

func isLetter(b byte) bool {
	return (b >= 'A' && b <= 'Z') || (b >= 'a' && b <= 'z')
}
func lower(b byte) byte {
	if b >= 'A' && b <= 'Z' {
		return b + 32
	}
	return b
}
func isUpper(b byte) bool {
	return b >= 'A' && b <= 'Z'
}

/* Year 1 – c‑reforms */
func transformYear1(word string) string {
	var out []byte
	i, n := 0, len(word)
	for i < n {
		ch := word[i]
		if ch == 'c' || ch == 'C' {
			if i+1 < n {
				next := word[i+1]
				lch := lower(ch)
				ln := lower(next)
				if ln == 'i' || ln == 'e' { // ci or ce
					if isUpper(ch) {
						out = append(out, 'S')
					} else {
						out = append(out, 's')
					}
					i++ // skip c, next char will be processed normally
				} else if ln == 'k' { // ck – omit c
					i++ // just skip c, keep next char for later
				} else { // other c
					if isUpper(ch) {
						out = append(out, 'K')
					} else {
						out = append(out, 'k')
					}
					i++
				}
			} else { // last character c
				if isUpper(ch) {
					out = append(out, 'K')
				} else {
					out = append(out, 'k')
				}
				i++
			}
		} else {
			out = append(out, ch)
			i++
		}
	}
	return string(out)
}

/* Year 2 – double letters */
func transformYear2(word string) string {
	s := word
	for {
		changed := false
		var new []byte
		i := 0
		for i < len(s) {
			if i+1 < len(s) && lower(s[i]) == lower(s[i+1]) {
				l := lower(s[i])
				if l == 'e' {
					new = append(new, 'i')
				} else if l == 'o' {
					new = append(new, 'u')
				} else {
					new = append(new, s[i]) // keep first character, case preserved
				}
				i += 2
				changed = true
			} else {
				new = append(new, s[i])
				i++
			}
		}
		if !changed {
			break
		}
		s = string(new)
	}
	return s
}

/* Year 3 – remove trailing e */
func transformYear3(word string) string {
	if len(word) > 1 && word[len(word)-1] == 'e' {
		return word[:len(word)-1]
	}
	return word
}

/* Article detection */
func isArticle(word string) bool {
	lw := strings.ToLower(word)
	return lw == "a" || lw == "an" || lw == "the"
}

func main() {
	// read whole input (one line)
	data, _ := io.ReadAll(os.Stdin)
	input := strings.TrimRight(string(data), "\r\n")

	var out []byte
	i := 0
	n := len(input)
	for i < n {
		if isLetter(input[i]) {
			start := i
			for i < n && isLetter(input[i]) {
				i++
			}
			orig := input[start:i]

			// apply the reforms
			trans := transformYear1(orig)
			trans = transformYear2(trans)
			trans = transformYear3(trans)

			if !isArticle(orig) {
				out = append(out, []byte(trans)...)
			}
		} else {
			out = append(out, input[i])
			i++
		}
	}
	result := strings.TrimSpace(string(out))
	fmt.Println(result)
}
