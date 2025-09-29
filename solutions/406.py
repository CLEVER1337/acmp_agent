
import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    
    freq_expected = []
    letters = []
    for i in range(1, n+1):
        parts = data[i].split()
        letter = parts[0]
        freq = float(parts[1])
        letters.append(letter)
        freq_expected.append(freq)
    
    cipher_text = data[n+1].strip()
    
    freq_observed = [0] * n
    total_chars = len(cipher_text)
    
    char_to_index = {}
    for i, c in enumerate(letters):
        char_to_index[c] = i
    
    for c in cipher_text:
        if c in char_to_index:
            idx = char_to_index[c]
            freq_observed[idx] += 1
    
    for i in range(n):
        freq_observed[i] /= total_chars
    
    sorted_expected_indices = sorted(range(n), key=lambda i: freq_expected[i])
    sorted_observed_indices = sorted(range(n), key=lambda i: freq_observed[i])
    
    mapping = {}
    for obs_idx, exp_idx in zip(sorted_observed_indices, sorted_expected_indices):
        cipher_char = letters[obs_idx]
        plain_char = letters[exp_idx]
        mapping[cipher_char] = plain_char
    
    for letter in letters:
        print(mapping[letter])

if __name__ == "__main__":
    main()
