
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, m, x = map(int, data[0].split())
    strings = data[1:1+n]
    
    hash_count = {}
    
    for s in strings:
        hash_val = 0
        power = 1
        for char in s:
            digit = int(char)
            hash_val = (hash_val + digit * power) % m
            power = (power * x) % m
            
        hash_count[hash_val] = hash_count.get(hash_val, 0) + 1
    
    pairs = 0
    for count in hash_count.values():
        if count > 1:
            pairs += count * (count - 1) // 2
            
    print(pairs)

if __name__ == "__main__":
    main()
