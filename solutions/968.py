
def main():
    import sys
    data = sys.stdin.read().splitlines()
    SA = data[0].strip()
    SB = data[1].strip()
    n = len(SA)
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char_to_index = {char: idx for idx, char in enumerate(alphabet)}
    total_chars = 26
    
    def dist(c1, c2):
        idx1 = char_to_index[c1]
        idx2 = char_to_index[c2]
        diff = abs(idx1 - idx2)
        return min(diff, total_chars - diff)
    
    total_sum = 0
    for shift in range(n):
        current_sum = 0
        for i in range(n):
            j = (i + shift) % n
            current_sum += dist(SA[i], SB[j])
        total_sum += current_sum
    
    print(total_sum)

if __name__ == "__main__":
    main()
