
import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    freq_info = []
    for i in range(1, 1 + n):
        parts = data[i].split()
        char = parts[0]
        freq = float(parts[1])
        freq_info.append((char, freq))
    
    encrypted_text = data[1 + n].strip()
    
    from collections import defaultdict
    encrypted_count = defaultdict(int)
    for c in encrypted_text:
        encrypted_count[c] += 1
    
    encrypted_chars = sorted(encrypted_count.keys())
    encrypted_freqs = []
    for c in encrypted_chars:
        freq = encrypted_count[c] / m
        encrypted_freqs.append((c, freq))
    
    sorted_original = sorted(freq_info, key=lambda x: x[1])
    sorted_encrypted = sorted(encrypted_freqs, key=lambda x: x[1])
    
    mapping = {}
    for i in range(len(sorted_encrypted)):
        encrypted_char = sorted_encrypted[i][0]
        original_char = sorted_original[i][0]
        mapping[encrypted_char] = original_char
    
    result = []
    for c in encrypted_chars:
        result.append(mapping[c])
    
    for char in result:
        print(char)

if __name__ == "__main__":
    main()
