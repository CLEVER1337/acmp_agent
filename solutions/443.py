
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    first_line = data[0].split()
    n = int(first_line[0])
    m = int(first_line[1])
    x = int(first_line[2])
    
    hashes = []
    for i in range(1, n + 1):
        s = data[i].strip()
        h = 0
        power = 1
        for char in s:
            digit = int(char)
            h = (h + digit * power) % m
            power = (power * x) % m
        hashes.append(h)
    
    count_dict = {}
    for h in hashes:
        count_dict[h] = count_dict.get(h, 0) + 1
        
    pairs = 0
    for count in count_dict.values():
        if count > 1:
            pairs += count * (count - 1) // 2
            
    print(pairs)

if __name__ == "__main__":
    main()
