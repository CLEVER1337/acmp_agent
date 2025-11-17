
import sys

def solve() -> None:
    # read all lines, keep only non‑empty ones
    data = [line.rstrip('\n') for line in sys.stdin.read().splitlines()]
    # ignore possible blank lines at the beginning or between the two lines
    lines = [ln for ln in data if ln.strip() != ""]
    if len(lines) < 2:
        return

    # first two non‑empty lines
    s0, s1 = lines[0].strip(), lines[1].strip()

    # pattern contains a wildcard, word does not (according to the statement)
    if '?' in s0 or '*' in s0:
        pattern, word = s0, s1
    else:
        pattern, word = s1, s0

    m, n = len(pattern), len(word)

    # dp[i][j] – pattern[:i] matches word[:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # empty word: only '*' can disappear
    for i in range(1, m + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]   # '*' can be empty
        else:
            dp[i][0] = False

    # fill the table
    for i in range(1, m + 1):
        p = pattern[i - 1]
        for j in range(1, n + 1):
            if p == '*':
                # star matches empty (dp[i-1][j]) or one more character (dp[i][j-1])
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p == '?':
                # '?' matches exactly one arbitrary character
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # ordinary letter must be equal
                dp[i][j] = dp[i - 1][j - 1] and p == word[j - 1]

    sys.stdout.write("YES\n" if dp[m][n] else "NO\n")

if __name__ == '__main__':
    solve()
