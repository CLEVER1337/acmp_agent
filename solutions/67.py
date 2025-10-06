
def ip_to_bin(ip):
    parts = list(map(int, ip.split('.')))
    return (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]

def main():
    import sys
    data = sys.stdin.read().splitlines()
    
    n = int(data[0])
    masks = []
    for i in range(1, n + 1):
        mask_str = data[i]
        masks.append(ip_to_bin(mask_str))
    
    m = int(data[n + 1])
    pairs = []
    for i in range(n + 2, n + 2 + m):
        ip1, ip2 = data[i].split()
        bin_ip1 = ip_to_bin(ip1)
        bin_ip2 = ip_to_bin(ip2)
        pairs.append((bin_ip1, bin_ip2))
    
    results = []
    for ip1, ip2 in pairs:
        count = 0
        for mask in masks:
            if (ip1 & mask) == (ip2 & mask):
                count += 1
        results.append(str(count))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
