
import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    
    freq_known = []
    for i in range(1, 1 + n):
        parts = data[i].split()
        char = parts[0]
        freq = float(parts[1])
        freq_known.append((char, freq))
    
    encrypted_text = data[1 + n].strip()
    
    freq_encrypted = {}
    for char in encrypted_text:
        freq_encrypted[char] = freq_encrypted.get(char, 0) + 1
    
    total_chars = len(encrypted_text)
    freq_encrypted_normalized = []
    for char, count in freq_encrypted.items():
        freq_encrypted_normalized.append((char, count / total_chars))
    
    freq_encrypted_normalized.sort(key=lambda x: x[1], reverse=True)
    freq_known.sort(key=lambda x: x[1], reverse=True)
    
    mapping = {}
    for i in range(len(freq_encrypted_normalized)):
        encrypted_char = freq_encrypted_normalized[i][0]
        known_char = freq_known[i][0]
        mapping[encrypted_char] = known_char
    
    result = []
    for encrypted_char, _ in freq_encrypted_normalized:
        result.append(mapping[encrypted_char])
    
    for char in result:
        print(char)

if __name__ == "__main__":
    main()
