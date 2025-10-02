
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, m, x = map(int, data[0].split())
    strings = data[1:1+n]
    
    hash_counts = {}
    
    for s in strings:
        hash_val = 0
        power = 1
        for char in s:
            digit = int(char)
            hash_val = (hash_val + digit * power) % m
            power = (power * x) % m
            
        hash_counts[hash_val] = hash_counts.get(hash_val, 0) + 1
        
    count = 0
    for freq in hash_counts.values():
        count += freq * (freq - 1) // 2
        
    print(count)

if __name__ == "__main__":
    main()
