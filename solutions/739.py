
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    K = int(data[0].strip())
    s = data[1].strip()
    n = len(s)
    if K == 0:
        print(s)
        return
        
    res = []
    used = [-1] * n
    for i in range(n):
        best_char = 'z'
        best_pos = -1
        for j in range(max(0, i - K), min(n, i + K + 1)):
            if used[j] == -1 and s[j] < best_char:
                best_char = s[j]
                best_pos = j
        if best_pos == -1:
            for j in range(max(0, i - K), min(n, i + K + 1)):
                if used[j] == -1:
                    best_char = s[j]
                    best_pos = j
        res.append(best_char)
        used[best_pos] = i
        
    print(''.join(res))

if __name__ == "__main__":
    main()
